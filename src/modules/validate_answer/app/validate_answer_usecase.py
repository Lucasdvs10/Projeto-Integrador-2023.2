from src.shared.domain.repositories.answer_repository_interface import IAnswerRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from fastapi import HTTPException, status

class ValidateAnswerUsecase:
    def __init__(self, answer_repository: IAnswerRepository, user_repository: IUserRepository):
        self.answer_repository = answer_repository
        self.user_repository = user_repository

    def __call__(self, answer_id: str):
        answer = self.answer_repository.get_answer(answer_id)
        if not answer:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Answer not found")
        user = self.user_repository.get_user_by_email(answer.email)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        if answer.is_right == 1:
            if answer.exercise_id in user.exercises_solved:
                user.exercises_solved.remove(answer.exercise_id)
        else:
            user.exercises_solved.append(answer.exercise_id)
                
        self.user_repository.update_user_by_email(user.email, new_exercises_solved=user.exercises_solved)
         
        new_is_right = abs(answer.is_right - 1)
        updated_answer = self.answer_repository.update_answer(answer_id, new_is_right=new_is_right)

        return updated_answer
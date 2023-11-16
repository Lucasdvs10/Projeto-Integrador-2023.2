from src.modules.create_exercise.app.create_exercise_usecase import CreateExerciseUseCase
from src.modules.create_exercise.app.create_exercise_viewmodel import CreateExerciseViewmodel
from src.shared.infra.repositories.exercise_repository_mock import ExerciseRepositoryMock


class Test_CreateExerciseViewmodel:
    def test_create_exercise_viewmodel(self):
        repo = ExerciseRepositoryMock()
        usecase = CreateExerciseUseCase(repo)
        new_exercise = usecase(exercise_id="1", title="title", enunciado="enunciado", creation_date=1577847600000, expiration_date=3387133800000, correct_answer="correct_answer")
        viewmodel = CreateExerciseViewmodel(new_exercise).to_dict()
        expected = {'exercise': {'exercise_id': '1', 'title': 'title', 'enunciado': 'enunciado', 'creation_date': 1577847600000, 'expiration_date': 3387133800000, 'correct_answer': 'correct_answer'}, 'message': 'Exercise created successfully'}
        
        assert viewmodel == expected
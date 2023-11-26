from src.shared.domain.entities.exercise import Exercise
from src.shared.infra.dto.ExerciseMongoDTO import ExerciseMongoDTO


class Test_ExerciseMongoDTO:
        
        def test_exercise_mongo_dto_from_entity(self):
            exercise = Exercise(
                exercise_id="1",
                title="Exercício 1",
                enunciado="Enunciado 1",
                creation_date=1701022536609,
                expiration_date=1701024536609,
                correct_answer="Resposta 1"
            )
            
            exercise_mongo_dto = ExerciseMongoDTO.from_entity(exercise)
            
            assert exercise_mongo_dto == ExerciseMongoDTO(exercise_id=exercise.exercise_id, title=exercise.title, enunciado=exercise.enunciado, creation_date=exercise.creation_date, expiration_date=exercise.expiration_date, correct_answer=exercise.correct_answer)
            
        def test_exercise_mongo_dto_to_entity(self):
            exercise_mongo_dto = ExerciseMongoDTO(
                exercise_id="1",
                title="Exercício 1",
                enunciado="Enunciado 1",
                creation_date=1701022536609,
                expiration_date=1701024536609,
                correct_answer="Resposta 1"
            )
            
            exercise = exercise_mongo_dto.to_entity()
            
            assert exercise == Exercise(exercise_id=exercise_mongo_dto.exercise_id, title=exercise_mongo_dto.title, enunciado=exercise_mongo_dto.enunciado, creation_date=exercise_mongo_dto.creation_date, expiration_date=exercise_mongo_dto.expiration_date, correct_answer=exercise_mongo_dto.correct_answer)
            
        def test_exercise_mongo_dto_to_mongo(self):
            exercise_mongo_dto = ExerciseMongoDTO(
                exercise_id="1",
                title="Exercício 1",
                enunciado="Enunciado 1",
                creation_date=1701022536609,
                expiration_date=1701024536609,
                correct_answer="Resposta 1"
            )
            
            exercise = exercise_mongo_dto.to_mongo()
            
            assert exercise == {
                'exercise_id': exercise_mongo_dto.exercise_id,
                'title': exercise_mongo_dto.title,
                'enunciado': exercise_mongo_dto.enunciado,
                'creation_date': exercise_mongo_dto.creation_date,
                'expiration_date': exercise_mongo_dto.expiration_date,
                'correct_answer': exercise_mongo_dto.correct_answer
            }
            
        def test_exercise_mongo_dto_from_mongo(self):
            exercise = {
                'exercise_id': "1",
                'title': "Exercício 1",
                'enunciado': "Enunciado 1",
                'creation_date': 0,
                'expiration_date': 0,
                'correct_answer': "Resposta 1"
            }

            exercise_mongo_dto = ExerciseMongoDTO.from_mongo(exercise)
            
            assert exercise_mongo_dto == ExerciseMongoDTO(exercise_id=exercise['exercise_id'], title=exercise['title'], enunciado=exercise['enunciado'], creation_date=exercise['creation_date'], expiration_date=exercise['expiration_date'], correct_answer=exercise['correct_answer'])
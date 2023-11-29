from src.shared.domain.entities.schedule import Schedule


class ScheduleMongoDTO:
    url: str
    
    def __init__(self, url):
        self.url = url
        
    @staticmethod
    def from_entity(schedule: Schedule) -> 'ScheduleMongoDTO':
        return ScheduleMongoDTO(schedule.url)
    
    def to_mongo(self) -> dict:
        return {
            'url': self.url
        }
        
    @staticmethod
    def from_mongo(schedule: dict) -> 'ScheduleMongoDTO':
        return ScheduleMongoDTO(schedule['url'])
    
    def to_entity(self) -> Schedule:
        return Schedule(self.url)
    
    def __repr__(self):
        return f"ScheduleMongoDTO(url={self.url})"
    
    def __eq__(self, other):
        if not isinstance(other, ScheduleMongoDTO):
            return False
        return self.url == other.url
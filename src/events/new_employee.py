

from src.models.Employee import EmployeeBase
from src.models.Event import Event


class NewEmployee(Event):
    '''
    NewEmployee Event
    '''
    def __init__(self, name_event: str = 'NewEmployee') -> None:
        super().__init__(name_event)
    
    def run(self, employee: EmployeeBase) -> None: #type: ignore
        self.logging.info(' Employee logged  '.center(50, '-'))
        self.logging.info(f'[Employee]: {employee.employee_info.username.capitalize()}')
        self.logging.info(f'[Employee]: {employee.employee_info.type}') 
        self.logging.info(f'[Employee]: {employee.employee_info.id}') 
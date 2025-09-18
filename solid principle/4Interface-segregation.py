# Clients should not be forced to depend on interfaces they do not use


# violates ls principle

class Worker:
    def work(self):
        pass

    def attend_meeting(self):
        pass

    def write_report(self):
        pass

class Technician(Worker):
    def work(self):
        print("Fixing machines.")

    def attend_meeting(self):
        raise NotImplementedError("Technicians don't attend meetings.")

    def write_report(self):
        raise NotImplementedError("Technicians don't write reports.")
    
    
# liskov substitution compliant

from abc import ABC, abstractmethod

# Specific interfaces
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class MeetingParticipant(ABC):
    @abstractmethod
    def attend_meeting(self):
        pass

class ReportWriter(ABC):
    @abstractmethod
    def write_report(self):
        pass

# Concrete classes implement only what they need
class Technician(Workable):
    def work(self):
        print("Technician is fixing machines.")

class Manager(Workable, MeetingParticipant, ReportWriter):
    def work(self):
        print("Manager is planning tasks.")

    def attend_meeting(self):
        print("Manager is attending a meeting.")

    def write_report(self):
        print("Manager is writing a report.")


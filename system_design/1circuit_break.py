# stop hammering faling service with a circuit breaker
# it opens after repeated failures, block calls for a cooldown period, then half-opens to test recovery

import time
from typing import Callable, TypeVar, Any, Type, Union, Tuple

F = TypeVar("F",bound=Callable[...,Any])

class CircuitBreaker:
    """
    simple production ready circuit breaker.
        -closed : normal operation
        -open: block calls after too many failures
        - Half-open :allow one call to test recovery
    """
    def __init__(
        self,
        failures_threshold:int = 3,
        recovery_time:int = 5.0,
        exceptions: Union[Tuple[Type[BaseException],...], Type[BaseException] ] = Exception
        ):
        self.failures_threshold = failures_threshold
        self.recovery_time = recovery_time
        self.exceptions = exceptions
        self.failures = 0
        self.state = "CLOSED"
        self.last_failures_time = 0.0
        
    def _transition(self):
        if self.state == "OPEN" and (time.time() - self.last_failures_time >= self.recovery_time):
            self.state = "HALF-OPEN"
    def call(self, func:F, *args, **kwargs) -> Any:
        self._transition()
        if self.state =="OPEN":
            raise RuntimeError("Circuit Breaker: Open , blocking calls")
        try:
            result = func(*args, **kwargs)
            self.failures = 0
            if self.state == "HALF-OPEN":
                self.state = "CLOSED"
            print(self.failures)
            return result
        except self.exceptions as e:
            self.failures += 1
            self.last_failures_time = time.time()
            if self.failures >= self.failures_threshold:
                self.state = "OPEN"
            raise
        
if __name__ == "__main__":
    cb = CircuitBreaker(failures_threshold=2, recovery_time=3)
    
    counter = {"n":0}
    def flaky_task():
        counter["n"] +=1
        if counter["n"] > 3:
            raise RuntimeError("Service down")
        return "Service Ok"
    for i in range(5):
        try:
            print(cb.call(flaky_task))
        except Exception as e:
            print("danger", e)
        time.sleep(2)
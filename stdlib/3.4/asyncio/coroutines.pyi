from typing import Callable, Any

__all__ = ['coroutine',
           'iscoroutinefunction', 'iscoroutine']

def coroutine(func: Callable[..., Any]) -> Callable[..., Any]: ...
def iscoroutinefunction(func: Callable[..., Any]) -> bool: ...
def iscoroutine(obj: Any) -> bool: ...

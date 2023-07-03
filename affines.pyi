from typing import Any, Literal, Optional, Tuple

from nptyping import Float, NDArray, Shape

def decompose44(
    A44: NDArray[Shape["4, 4"], Float]
) -> Tuple[
    NDArray[Shape["3"], Float],
    NDArray[Shape["3, 3"], Float],
    NDArray[Shape["3"], Float],
    NDArray[Shape["3"], Float],
]: ...
def decompose(
    A: NDArray[Shape[Literal["N, N"]], Float]
) -> Tuple[
    NDArray[Shape[Literal["N-1"]], Float],
    NDArray[Shape[Literal["N-1, N-1"]], Float],
    NDArray[Shape[Literal["N-1"]], Float],
    NDArray[Shape[Literal["P"]], Float],
]: ...
def compose(
    T: NDArray[Shape[Literal["N"]], Float],
    R: NDArray[Shape[Literal["N, N"]], Float],
    Z: NDArray[Shape[Literal["N"]], Float],
    S: Optional[NDArray[Any, Float]] = None,
) -> NDArray[Shape[Literal["N+1, N+1"]], Float]: ...

from nptyping import Float, NDArray, Shape
from typing import Tuple, Any, Optional

def decompose44(
    A44: NDArray[Shape["4, 4"], Float]
) -> Tuple[
    NDArray[Shape["3,"], Float],
    NDArray[Shape["3, 3"], Float],
    NDArray[Shape["3,"], Float],
    NDArray[Shape["3,"], Float],
]: ...
def compose(
    T: NDArray[Shape["3,"], Float],
    R: NDArray[Shape["3, 3"], Float],
    Z: NDArray[Shape["3,"], Float],
    S: Optional[NDArray[Any, Float]] = None,
) -> NDArray[Shape["4, 4"], Float]: ...

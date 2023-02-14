from nptyping import Float, NDArray, Shape
from typing import Tuple

def euler2mat(
    ai: float, aj: float, ak: float, axes: str = "sxyz"
) -> NDArray[Shape["3, 3"], Float]: ...
def mat2euler(
    mat: NDArray[Shape["3, 3"], Float], axes: str = "sxyz"
) -> Tuple[float, float, float]: ...

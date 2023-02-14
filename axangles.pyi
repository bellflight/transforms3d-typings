from nptyping import Float, NDArray, Shape
from typing import Tuple

def axangle2mat(
    axis: Tuple[float, float, float], angle: float, is_normalized: bool = False
) -> NDArray[Shape["3, 3"], Float]: ...

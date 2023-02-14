from nptyping import Float, NDArray, Shape
from typing import Tuple

def quat2mat(q: Tuple[float, float, float, float]) -> NDArray[Shape["3, 3"], Float]: ...

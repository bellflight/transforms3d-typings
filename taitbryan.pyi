from typing import Optional, Tuple

from nptyping import Float, NDArray, Shape

def euler2mat(z: float, y: float, x: float) -> NDArray[Shape["3, 3"], Float]: ...
def mat2euler(
    M: NDArray[Shape["3, 3"], Float], cy_thresh: Optional[float]
) -> Tuple[float, float, float]: ...
def euler2quat(z: float, y: float, x: float) -> NDArray[Shape["4"], Float]: ...
def quat2euler(q: NDArray[Shape["4"], Float]) -> Tuple[float, float, float]: ...
def euler2axangle(
    z: float, y: float, x: float
) -> Tuple[NDArray[Shape["3"], Float], float]: ...
def axangle2euler(
    vector: NDArray[Shape["3"], Float], theta: float
) -> Tuple[float, float, float]: ...

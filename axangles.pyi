from typing import Optional, Tuple

from nptyping import Float, NDArray, Shape

def axangle2mat(
    axis: NDArray[Shape["3"], Float], angle: float, is_normalized: bool = False
) -> NDArray[Shape["3, 3"], Float]: ...
def axangle2aff(
    axis: NDArray[Shape["3"], Float],
    angle: float,
    point: Optional[NDArray[Shape["3"], Float]] = None,
) -> NDArray[Shape["4, 4"], Float]: ...
def mat2axangle(
    mat: NDArray[Shape["3, 3"], Float], unit_thresh: float = 1e-5
) -> Tuple[NDArray[Shape["3"], Float], float]: ...
def aff2axangle(
    aff: NDArray[Shape["4, 4"], Float]
) -> Tuple[NDArray[Shape["3"], Float], float, NDArray[Shape["3"], Float]]: ...

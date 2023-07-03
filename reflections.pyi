from typing import Optional, Tuple

from nptyping import Float, NDArray, Shape

def rfnorm2mat(normal: NDArray[Shape["3"], Float]) -> NDArray[Shape["3, 3"], Float]: ...
def rfnorm2aff(
    normal: NDArray[Shape["3"], Float],
    point: Optional[NDArray[Shape["3, 3"], Float]] = None,
) -> NDArray[Shape["4, 4"], Float]: ...
def mat2rfnorm(mat: NDArray[Shape["3, 3"], Float]) -> NDArray[Shape["3"], Float]: ...
def aff2rfnorm(
    aff: NDArray[Shape["4, 4"], Float]
) -> Tuple[NDArray[Shape["3"], Float], NDArray[Shape["3"], Float]]: ...

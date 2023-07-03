from typing import Optional, Tuple

from nptyping import Float, NDArray, Shape

def zfdir2mat(
    factor: float, direction: Optional[NDArray[Shape["3"], Float]] = None
) -> NDArray[Shape["3, 3"], Float]: ...
def zfdir2aff(
    factor: float,
    direction: Optional[NDArray[Shape["3"], Float]] = None,
    origin: Optional[NDArray[Shape["3"], Float]] = None,
) -> NDArray[Shape["4, 4"], Float]: ...
def mat2zfdir(
    mat: NDArray[Shape["3, 3"], Float]
) -> Tuple[float, Optional[NDArray[Shape["3"], Float]]]: ...
def aff2zfdir(
    aff: NDArray[Shape["4, 4"], Float]
) -> Tuple[float, Optional[NDArray[Shape["3"], Float]], NDArray[Shape["3"], Float]]: ...

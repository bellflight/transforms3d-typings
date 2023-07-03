from typing import Literal, Optional, Tuple

from nptyping import Float, NDArray, Shape

def striu2mat(
    striu: NDArray[Shape[Literal["N"]], Float]
) -> NDArray[Shape[Literal["N, N"]], Float]: ...
def sadn2mat(
    angle: float,
    direction: NDArray[Shape["3"], Float],
    normal: NDArray[Shape["3"], Float],
) -> NDArray[Shape["3, 3"], Float]: ...
def sadn2aff(
    angle: float,
    direction: NDArray[Shape["3"], Float],
    normal: NDArray[Shape["3"], Float],
    point: Optional[NDArray[Shape["3"], Float]] = None,
) -> NDArray[Shape["4, 4"], Float]: ...
def inverse_outer(
    mat: NDArray[Shape["3, 3"], Float]
) -> Tuple[float, NDArray[Shape["3"], Float], NDArray[Shape["3"], Float]]: ...
def mat2sadn(
    mat: NDArray[Shape["3, 3"], Float]
) -> Tuple[float, NDArray[Shape["3"], Float], NDArray[Shape["3"], Float]]: ...
def aff2sadn(
    aff: NDArray[Shape["3, 3"], Float]
) -> Tuple[
    float,
    NDArray[Shape["3"], Float],
    NDArray[Shape["3"], Float],
    NDArray[Shape["3"], Float],
]: ...

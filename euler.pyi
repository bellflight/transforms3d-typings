from typing import Literal, Tuple, Union

from nptyping import Float, NDArray, Shape

_axes_literal = Literal[
    "sxyz",
    "sxyx",
    "sxzy",
    "sxzx",
    "syzx",
    "syzy",
    "syxz",
    "syxy",
    "szxy",
    "szxz",
    "szyx",
    "szyz",
    "rzyx",
    "rxyx",
    "ryzx",
    "rxzx",
    "rxzy",
    "ryzy",
    "rzxy",
    "ryxy",
    "ryxz",
    "rzxz",
    "rxyz",
    "rzyz",
]

def euler2mat(
    ai: float, aj: float, ak: float, axes: _axes_literal = "sxyz"
) -> NDArray[Shape["3, 3"], Float]: ...
def mat2euler(
    mat: Union[NDArray[Shape["3, 3"], Float], NDArray[Shape["4, 4"], Float]],
    axes: _axes_literal = "sxyz",
) -> Tuple[float, float, float]: ...
def euler2quat(
    ai: float, aj: float, ak: float, axes: _axes_literal = "sxyz"
) -> NDArray[Shape["4"], Float]: ...
def quat2euler(
    quaternion: NDArray[Shape["4"], Float], axes: _axes_literal = "sxyz"
) -> Tuple[float, float, float]: ...
def euler2axangle(
    ai: float, aj: float, ak: float, axes: _axes_literal = "sxyz"
) -> Tuple[NDArray[Shape["3"], Float], float]: ...
def axangle2euler(
    vector: NDArray[Shape["3"], Float], theta: float, axes: _axes_literal = "sxyz"
) -> Tuple[float, float, float]: ...

class EulerFuncs(object):
    def euler2mat(
        self, ai: float, aj: float, ak: float, axes: _axes_literal = "sxyz"
    ) -> NDArray[Shape["3, 3"], Float]: ...
    def mat2euler(
        self,
        mat: Union[NDArray[Shape["3, 3"], Float], NDArray[Shape["4, 4"], Float]],
        axes: _axes_literal = "sxyz",
    ) -> Tuple[float, float, float]: ...
    def euler2quat(
        self, ai: float, aj: float, ak: float, axes: _axes_literal = "sxyz"
    ) -> NDArray[Shape["4"], Float]: ...
    def quat2euler(
        self, quat: NDArray[Shape["4"], Float], axes: _axes_literal = "sxyz"
    ) -> Tuple[float, float, float]: ...
    def euler2axangle(
        self, ai: float, aj: float, ak: float, axes: _axes_literal = "sxyz"
    ) -> Tuple[NDArray[Shape["3"], Float], float]: ...
    def axangle2euler(
        self,
        vector: NDArray[Shape["3"], Float],
        theta: float,
        axes: _axes_literal = "sxyz",
    ) -> Tuple[float, float, float]: ...

class TBZYX(EulerFuncs):
    def euler2mat(
        self, ai: float, aj: float, ak: float
    ) -> NDArray[Shape["3, 3"], Float]: ...
    def mat2euler(
        self, mat: NDArray[Shape["3, 3"], Float]
    ) -> Tuple[float, float, float]: ...
    def euler2quat(
        self, ai: float, aj: float, ak: float
    ) -> NDArray[Shape["4"], Float]: ...

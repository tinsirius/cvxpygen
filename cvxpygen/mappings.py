from dataclasses import dataclass, field

import scipy.sparse as sp
import numpy as np


@dataclass
class AffineMap:
    mapping_rows: list = field(default_factory=list)
    mapping: list = field(default_factory=list)
    indices: list = field(default_factory=list)
    indptr: list = field(default_factory=list)
    shape = ()


@dataclass
class ParameterCanon:
    p: dict = field(default_factory=dict)
    p_csc: dict[str, sp.csc_matrix] = field(default_factory=dict)
    p_id_to_mapping: dict[str, sp.csr_matrix] = field(default_factory=dict)
    p_id_to_changes: dict[str, bool] = field(default_factory=dict)
    p_id_to_size: dict[str, int] = field(default_factory=dict)
    nonzero_d = True


@dataclass
class ParameterInfo:
    col_to_name_usp: dict[int, str]
    flat_usp: np.ndarray
    id_to_col: dict[int, int]
    ids: list[int]
    name_to_shape: dict[str, tuple]
    name_to_size_usp: dict[str, int]
    name_to_sparsity: dict[str, np.ndarray]
    name_to_sparsity_type: dict[str, str]
    names: list[str]
    num: int
    sparsity_mask: np.ndarray
    writable: dict[str, np.ndarray]


@dataclass
class VariableInfo:
    name_to_offset: dict[str, int]
    name_to_indices: dict[str, np.ndarray]
    name_to_size: dict[str, int]
    sizes: list[int]
    name_to_shape: dict[str, tuple]
    name_to_init: dict[str, np.ndarray]


@dataclass
class PrimalVariableInfo(VariableInfo):
    name_to_sym: dict[str, bool]
    sym: list[bool]


@dataclass
class DualVariableInfo(VariableInfo):
    name_to_vec: dict[str, str]


@dataclass
class ConstraintInfo:
    n_data_constr: int
    n_data_constr_mat: int
    mapping_rows_eq: np.ndarray
    mapping_rows_ineq: np.ndarray

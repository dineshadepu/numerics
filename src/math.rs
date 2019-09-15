use pyo3::prelude::*;
// use numpy::{PyArrayDyn};
use numpy::{IntoPyArray, PyArrayDyn};
use ndarray::{ArrayD, ArrayViewD, ArrayViewMutD, Array, aview1, ArrayView1};


fn norm(x: ArrayViewD<'_, f64>) -> f64{
    let mut result = 0.;
    for i in 0..x.len(){
        result += x[i]*x[i];
    }
    result.sqrt()
}

#[pyfunction]
fn py_norm(
    x: &PyArrayDyn<f64>,
) -> PyResult<f64> {
    let x = x.as_array();
    return Ok(norm(x));
}

/// This module contains functions for displaying alerts.
#[pymodule(math)]
fn init(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(py_norm))?;
    Ok(())
}


// ----------------------------------
// tests rust functions
// #[test]
// fn test_norm(){
//     let x = Array::range(0., 10., 0.5);
// }

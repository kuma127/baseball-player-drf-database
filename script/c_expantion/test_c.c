#include <Python.h>

static PyObject *

test_c(PyObject *self, PyObject *args) {
    const char *text;
    if (!PyArg_ParseTuple(args, "s", &text))
        return NULL;
    printf("%s\n", text);
    Py_RETURN_NONE;
}

static PyMethodDef test_c_methods[] = {
    {"print", test_c, METH_VARARGS, "test c"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef test_c_module = {
    PyModuleDef_HEAD_INIT,
    "test_c",
    "test c extention",
    -1,
    test_c_methods
};

PyMODINIT_FUNC
PyInit_test_c(void) {
    return PyModule_Create(&test_c_module);
}
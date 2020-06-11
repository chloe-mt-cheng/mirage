#! /usr/bin/env python
"""Test the catalog generation functionality in Mirage

Authors
-------
    - Bryan Hilbert

Use
---
    >>> pytest -s test_catalog_generation.py


"""

from mirage.utils import utils


def test_make_mag_column_names():
    instrument = 'nircam'
    filters = ['F090W/CLEAR', 'F090W/WLP8', 'WLM8/F115W', 'F322W2/F323N', 'F444W/F405N', 'F470N/F444W', 'F444W/CLEAR', 'CLEAR/F150W']
    std_filters = utils.standardize_filters(instrument, filters)
    cols = utils.make_mag_column_names(instrument, std_filters)

    truth = ['nircam_f090w_clear_magnitude', 'nircam_f090w_wlp8_magnitude', 'nircam_f115w_wlm8_magnitude',
             'nircam_f322w2_f323n_magnitude', 'nircam_f444w_f405n_magnitude', 'nircam_f444w_f470n_magnitude',
             'nircam_f444w_clear_magnitude', 'nircam_f150w_clear_magnitude']
    for val, check_val in zip(cols, truth):
        assert val == check_val

    instrument = 'niriss'
    filters = ['F090W', 'F150W/CLEAR', 'F277W/CLEAR', 'CLEAR/F430M']
    std_filters = utils.standardize_filters(instrument, filters)
    cols = utils.make_mag_column_names(instrument, std_filters)

    truth = ['niriss_f090w_magnitude', 'niriss_f150w_magnitude', 'niriss_f277w_magnitude', 'niriss_f430m_magnitude']
    for val, check_val in zip(cols, truth):
        assert val == check_val

    instrument = 'fgs'
    filters = ['guider1', 'guider2']
    std_filters = utils.standardize_filters(instrument, filters)
    cols = utils.make_mag_column_names(instrument, std_filters)

    truth = ['fgs_guider1_magnitude', 'fgs_guider2_magnitude']
    for val, check_val in zip(cols, truth):
        assert val == check_val

def test_standardize_filters():
    instrument = 'nircam'
    filters = ['F090W', 'F070W/CLEAR', 'CLEAR/F444W', 'F090W/WLP8', 'WLM8/F115W', 'F322W2/F323N', 'F470N/F444W']
    std_nircam = utils.standardize_filters(instrument, filters)

    truth = ['F090W/CLEAR', 'F070W/CLEAR', 'F444W/CLEAR', 'F090W/WLP8', 'F115W/WLM8', 'F322W2/F323N', 'F444W/F470N']
    for std, expected in zip(std_nircam, truth):
        assert std == expected

    instrument = 'niriss'
    filters = ['F090W', 'F115W/CLEAR', 'CLEAR/']




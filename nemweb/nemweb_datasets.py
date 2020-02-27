from collections import namedtuple

#  class factory function for containing data for 'Current' datasets
CurrentDataset = namedtuple("NemwebCurrentFile",
                            ["dataset_name",
                             "nemfile_pattern",
                             "datetime_format",
                             "datetime_column",
                             "tables"])

DATASETS = {
    "dispatch_scada": CurrentDataset(
        dataset_name="Dispatch_SCADA",
        nemfile_pattern='PUBLIC_DISPATCHSCADA_([0-9]{12})_[0-9]{16}.zip',
        datetime_format="%Y%m%d%H%M",
        datetime_column="SETTLEMENTDATE",
        tables=["DISPATCH_UNIT_SCADA"]),

    "trading_is":    CurrentDataset(
        dataset_name="TradingIS_Reports",
        nemfile_pattern="PUBLIC_TRADINGIS_([0-9]{12})_[0-9]{16}.zip",
        datetime_format="%Y%m%d%H%M",
        datetime_column="SETTLEMENTDATE",
        tables=['TRADING_PRICE',
                'TRADING_REGIONSUM',
                'TRADING_INTERCONNECTORRES']),

    "rooftopPV_actual": CurrentDataset(
        dataset_name="ROOFTOP_PV/ACTUAL",
        nemfile_pattern="PUBLIC_ROOFTOP_PV_ACTUAL_([0-9]{14})_[0-9]{16}.zip",
        datetime_format="%Y%m%d%H%M00",
        datetime_column="INTERVAL_DATETIME",
        tables=['ROOFTOP_ACTUAL']),

    "next_day_actual_gen": CurrentDataset(
        dataset_name="Next_Day_Actual_Gen",
        nemfile_pattern="PUBLIC_NEXT_DAY_ACTUAL_GEN_([0-9]{8})_[0-9]{16}.zip",
        datetime_format="%Y%m%d",
        datetime_column="INTERVAL_DATETIME",
        tables=['METER_DATA_GEN_DUID']),

    "dispatch_is": CurrentDataset(
        dataset_name="DispatchIS_Reports",
        nemfile_pattern="PUBLIC_DISPATCHIS_([0-9]{12})_[0-9]{16}.zip",
        datetime_format="%Y%m%d%H%M",
        datetime_column="SETTLEMENTDATE",
        tables=['DISPATCH_PRICE',
                'DISPATCH_REGIONSUM',
                'DISPATCH_INTERCONNECTORRES']),

    "next_day_dispatch": CurrentDataset(
        dataset_name="Next_Day_Dispatch",
        nemfile_pattern="PUBLIC_NEXT_DAY_DISPATCH_([0-9]{8})_[0-9]{16}.zip",
        datetime_format="%Y%m%d",
        datetime_column="SETTLEMENTDATE",
        tables=['DISPATCH_UNIT_SOLUTION']),

    "p5_min": CurrentDataset(
        dataset_name="P5_Reports",
        nemfile_pattern="PUBLIC_P5MIN_([0-9]{12})_[0-9]{14}.zip",
        datetime_format="%Y%m%d%H%M",
        datetime_column="RUN_DATETIME",
        tables=['P5MIN_CASESOLUTION',
                'P5MIN_LOCAL_PRICE',
                'P5MIN_REGIONSOLUTION',
                'P5MIN_INTERCONNECTORSOLN',
                'P5MIN_CONSTRAINTSOLUTION']),
}

from pycromanager import JavaBackendAcquisition, multi_d_acquisition_events


with JavaBackendAcquisition(directory=r"/Users/henrypinkard/tmp", name="tcz_acq", debug=False) as acq:
    # Generate the events for a single z-stack
    events = multi_d_acquisition_events(
        num_time_points=8,
        time_interval_s=0,
        channel_group="Channel",
        channels=["DAPI", "FITC"],
        z_start=0,
        z_end=6,
        z_step=0.4,
        order="tcz",
    )
    acq.acquire(events)

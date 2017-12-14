import pytest

import pkg_resources
import os
import warnings

warnings.simplefilter("ignore")

example_file_path = pkg_resources.resource_filename(
    'protozfitsreader',
    os.path.join(
        'tests',
        'resources',
        'example_10evts.fits.fz'
    )
)

FIRST_EVENT_IN_EXAMPLE_FILE = 97750287
TELESCOPE_ID_IN_EXAMPLE_FILE = 1
EVENTS_IN_EXAMPLE_FILE = 10
EXPECTED_LOCAL_TIME = [
    1.5094154944067896e+18,
    1.509415494408104e+18,
    1.509415494408684e+18,
    1.509415494415717e+18,
    1.5094154944180828e+18,
    1.5094154944218719e+18,
    1.5094154944245553e+18,
    1.5094154944267853e+18,
    1.509415494438982e+18,
    1.5094154944452902e+18
]
EXPECTED_GPS_TIME = [0] * EVENTS_IN_EXAMPLE_FILE


def test_rawreader_can_work_with_relative_path():
    from protozfitsreader import rawzfitsreader
    from protozfitsreader import L0_pb2

    relative_test_file_path = os.path.relpath(example_file_path)
    rawzfitsreader.open(relative_test_file_path + ':Events')
    raw = rawzfitsreader.readEvent()
    assert rawzfitsreader.getNumRows() == EVENTS_IN_EXAMPLE_FILE

    event = L0_pb2.CameraEvent()
    event.ParseFromString(raw)


def test_examplefile_has_no_runheader():
    from protozfitsreader import rawzfitsreader
    from protozfitsreader import L0_pb2

    rawzfitsreader.open(example_file_path + ':RunHeader')

    raw = rawzfitsreader.readEvent()
    assert raw < 0

    header = L0_pb2.CameraRunHeader()
    with pytest.raises(TypeError):
        header.ParseFromString(raw)


def test_rawreader_can_work_with_absolute_path():
    from protozfitsreader import rawzfitsreader
    from protozfitsreader import L0_pb2

    rawzfitsreader.open(example_file_path + ':Events')
    raw = rawzfitsreader.readEvent()
    assert rawzfitsreader.getNumRows() == EVENTS_IN_EXAMPLE_FILE

    event = L0_pb2.CameraEvent()
    event.ParseFromString(raw)


def test_rawreader_can_iterate():
    from protozfitsreader import rawzfitsreader
    from protozfitsreader import L0_pb2

    rawzfitsreader.open(example_file_path + ':Events')
    for i in range(rawzfitsreader.getNumRows()):
        event = L0_pb2.CameraEvent()
        event.ParseFromString(rawzfitsreader.readEvent())
        assert event.eventNumber == i + FIRST_EVENT_IN_EXAMPLE_FILE


def test_event_has_certain_fields():
    from protozfitsreader import rawzfitsreader
    from protozfitsreader import L0_pb2

    '''
    These fields seem to be non-empty:
        event.eventNumber
        event.telescopeID
        event.trig.timeSec
        event.trig.timeNanoSec
        event.local_time_sec
        event.local_time_nanosec
        event.event_type
        event.eventType
        event.head.numGainChannels
        event.hiGain.waveforms
        event.trigger_input_traces
        event.trigger_output_patch7
        event.trigger_output_patch19
        event.pixels_flags
    '''

    rawzfitsreader.open(example_file_path + ':Events')
    for i in range(rawzfitsreader.getNumRows()):
        event = L0_pb2.CameraEvent()
        event.ParseFromString(rawzfitsreader.readEvent())

        assert event.eventNumber is not None
        assert event.telescopeID is not None
        assert event.trig.timeSec is not None
        assert event.trig.timeNanoSec is not None
        assert event.local_time_sec is not None
        assert event.local_time_nanosec is not None
        assert event.event_type is not None
        assert event.eventType is not None
        assert event.head.numGainChannels is not None
        assert event.hiGain.waveforms is not None
        assert event.trigger_input_traces is not None
        assert event.trigger_output_patch7 is not None
        assert event.trigger_output_patch19 is not None
        assert event.pixels_flags is not None

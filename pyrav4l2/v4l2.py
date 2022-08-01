import ctypes

#
# Enums
#
# v4l2_buf_type
V4L2_BUF_TYPE_VIDEO_CAPTURE = 1
V4L2_BUF_TYPE_VIDEO_OUTPUT = 2
V4L2_BUF_TYPE_VIDEO_OVERLAY = 3
V4L2_BUF_TYPE_VBI_CAPTURE = 4
V4L2_BUF_TYPE_VBI_OUTPUT = 5
V4L2_BUF_TYPE_SLICED_VBI_CAPTURE = 6
V4L2_BUF_TYPE_SLICED_VBI_OUTPUT = 7
V4L2_BUF_TYPE_VIDEO_OUTPUT_OVERLAY = 8
V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE = 9
V4L2_BUF_TYPE_VIDEO_OUTPUT_MPLANE = 10
V4L2_BUF_TYPE_SDR_CAPTURE = 11
V4L2_BUF_TYPE_SDR_OUTPUT = 12
V4L2_BUF_TYPE_META_CAPTURE = 13
V4L2_BUF_TYPE_META_OUTPUT = 14

# v4l2_field
V4L2_FIELD_ANY = 0
V4L2_FIELD_NONE = 1
V4L2_FIELD_TOP = 2
V4L2_FIELD_BOTTOM = 3
V4L2_FIELD_INTERLACED = 4
V4L2_FIELD_SEQ_TB = 5
V4L2_FIELD_SEQ_BT = 6
V4L2_FIELD_ALTERNATE = 7
V4L2_FIELD_INTERLACED_TB = 8
V4L2_FIELD_INTERLACED_BT = 9

# v4l2_ctrl_type
V4L2_CTRL_TYPE_INTEGER = 1
V4L2_CTRL_TYPE_BOOLEAN = 2
V4L2_CTRL_TYPE_MENU = 3
V4L2_CTRL_TYPE_BUTTON = 4
V4L2_CTRL_TYPE_INTEGER64 = 5
V4L2_CTRL_TYPE_CTRL_CLASS = 6
V4L2_CTRL_TYPE_STRING = 7
V4L2_CTRL_TYPE_BITMASK = 8
V4L2_CTRL_TYPE_INTEGER_MENU = 9

# Compound types are >= 0x0100
V4L2_CTRL_COMPOUND_TYPES = 0x0100
V4L2_CTRL_TYPE_U8 = 0x0100
V4L2_CTRL_TYPE_U16 = 0x0101
V4L2_CTRL_TYPE_U32 = 0x0102
V4L2_CTRL_TYPE_AREA = 0x0106

V4L2_CTRL_TYPE_HDR10_CLL_INFO = 0x0110
V4L2_CTRL_TYPE_HDR10_MASTERING_DISPLAY = 0x0111

V4L2_CTRL_TYPE_H264_SPS = 0x0200
V4L2_CTRL_TYPE_H264_PPS = 0x0201
V4L2_CTRL_TYPE_H264_SCALING_MATRIX = 0x0202
V4L2_CTRL_TYPE_H264_SLICE_PARAMS = 0x0203
V4L2_CTRL_TYPE_H264_DECODE_PARAMS = 0x0204
V4L2_CTRL_TYPE_H264_PRED_WEIGHTS = 0x0205

V4L2_CTRL_TYPE_FWHT_PARAMS = 0x0220

V4L2_CTRL_TYPE_VP8_FRAME = 0x0240

V4L2_CTRL_TYPE_MPEG2_QUANTISATION = 0x0250
V4L2_CTRL_TYPE_MPEG2_SEQUENCE = 0x0251
V4L2_CTRL_TYPE_MPEG2_PICTURE = 0x0252

V4L2_CTRL_TYPE_VP9_COMPRESSED_HDR = 0x0260
V4L2_CTRL_TYPE_VP9_FRAME = 0x0261

#
# Flags
#

# Values for 'capabilities' field in v4l2_capability
V4L2_CAP_VIDEO_CAPTURE = 0x00000001  # Is a video capture device
V4L2_CAP_VIDEO_OUTPUT = 0x00000002  # Is a video output device
V4L2_CAP_VIDEO_OVERLAY = 0x00000004  # Can do video overlay
V4L2_CAP_VBI_CAPTURE = 0x00000010  # Is a raw VBI capture device
V4L2_CAP_VBI_OUTPUT = 0x00000020  # Is a raw VBI output device
V4L2_CAP_SLICED_VBI_CAPTURE = 0x00000040  # Is a sliced VBI capture device
V4L2_CAP_SLICED_VBI_OUTPUT = 0x00000080  # Is a sliced VBI output device
V4L2_CAP_RDS_CAPTURE = 0x00000100  # RDS data capture
V4L2_CAP_VIDEO_OUTPUT_OVERLAY = 0x00000200  # Can do video output overlay
V4L2_CAP_HW_FREQ_SEEK = 0x00000400  # Can do hardware frequency seek
V4L2_CAP_RDS_OUTPUT = 0x00000800  # Is an RDS encoder

V4L2_CAP_VIDEO_CAPTURE_MPLANE = 0x00001000
V4L2_CAP_VIDEO_OUTPUT_MPLANE = 0x00002000
V4L2_CAP_VIDEO_M2M_MPLANE = 0x00004000
V4L2_CAP_VIDEO_M2M = 0x00008000

V4L2_CAP_TUNER = 0x00010000  # has a tuner
V4L2_CAP_AUDIO = 0x00020000  # has audio support
V4L2_CAP_RADIO = 0x00040000  # is a radio device
V4L2_CAP_MODULATOR = 0x00080000  # has a modulator

V4L2_CAP_SDR_CAPTURE = 0x00100000  # Is a SDR capture device
V4L2_CAP_EXT_PIX_FORMAT = 0x00200000  # Supports the extended pixel format
V4L2_CAP_SDR_OUTPUT = 0x00400000  # Is a SDR output device
V4L2_CAP_META_CAPTURE = 0x00800000  # Is a metadata capture device

V4L2_CAP_READWRITE = 0x01000000  # read/write systemcalls
V4L2_CAP_ASYNCIO = 0x02000000  # async I/O
V4L2_CAP_STREAMING = 0x04000000  # streaming I/O ioctls
V4L2_CAP_META_OUTPUT = 0x08000000  # Is a metadata output device

V4L2_CAP_TOUCH = 0x10000000  # Is a touch device

V4L2_CAP_IO_MC = 0x20000000  # Is input/output controlled by the media controller

V4L2_CAP_DEVICE_CAPS = 0x80000000  # sets device capabilities field

# v4l2_fmtdesc flags
V4L2_FMT_FLAG_COMPRESSED = 0x0001
V4L2_FMT_FLAG_EMULATED = 0x0002
V4L2_FMT_FLAG_CONTINUOUS_BYTESTREAM = 0x0004
V4L2_FMT_FLAG_DYN_RESOLUTION = 0x0008
V4L2_FMT_FLAG_ENC_CAP_FRAME_INTERVAL = 0x0010
V4L2_FMT_FLAG_CSC_COLORSPACE = 0x0020
V4L2_FMT_FLAG_CSC_XFER_FUNC = 0x0040
V4L2_FMT_FLAG_CSC_YCBCR_ENC = 0x0080
V4L2_FMT_FLAG_CSC_HSV_ENC = V4L2_FMT_FLAG_CSC_YCBCR_ENC
V4L2_FMT_FLAG_CSC_QUANTIZATION = 0x0100

# Values for type field in v4l2_frmsizeenum
V4L2_FRMSIZE_TYPE_DISCRETE = 1
V4L2_FRMSIZE_TYPE_CONTINUOUS = 2
V4L2_FRMSIZE_TYPE_STEPWISE = 3

# Control flags
V4L2_CTRL_FLAG_DISABLED = 0x0001
V4L2_CTRL_FLAG_GRABBED = 0x0002
V4L2_CTRL_FLAG_READ_ONLY = 0x0004
V4L2_CTRL_FLAG_UPDATE = 0x0008
V4L2_CTRL_FLAG_INACTIVE = 0x0010
V4L2_CTRL_FLAG_SLIDER = 0x0020
V4L2_CTRL_FLAG_WRITE_ONLY = 0x0040
V4L2_CTRL_FLAG_VOLATILE = 0x0080
V4L2_CTRL_FLAG_HAS_PAYLOAD = 0x0100
V4L2_CTRL_FLAG_EXECUTE_ON_WRITE = 0x0200
V4L2_CTRL_FLAG_MODIFY_LAYOUT = 0x0400

#  Query flags, to be ORed with the control ID
V4L2_CTRL_FLAG_NEXT_CTRL = 0x80000000
V4L2_CTRL_FLAG_NEXT_COMPOUND = 0x40000000

#  User-class control IDs defined by V4L2
V4L2_CID_MAX_CTRLS = 1024
#  IDs reserved for driver specific controls
V4L2_CID_PRIVATE_BASE = 0x08000000

V4L2_CTRL_ID_MASK = 0x0fffffff


def V4L2_CTRL_ID2CLASS(id):
    return id & 0x0fff0000


def V4L2_CTRL_ID2WHICH(id):
    return id & 0x0fff0000


def V4L2_CTRL_DRIVER_PRIV(id):
    return id & 0xffff >= 0x1000


V4L2_CTRL_MAX_DIMS = 4
V4L2_CTRL_WHICH_CUR_VAL = 0
V4L2_CTRL_WHICH_DEF_VAL = 0x0f000000
V4L2_CTRL_WHICH_REQUEST_VAL = 0x0f010000

# v4l2_memory
V4L2_MEMORY_MMAP = 1
V4L2_MEMORY_USERPTR = 2
V4L2_MEMORY_OVERLAY = 3
V4L2_MEMORY_DMABUF = 4


#
# v4l structures
#
class v4l2_pix_format(ctypes.Structure):

    class _encoding(ctypes.Union):
        _fields_ = [
            ("ycbcr_enc", ctypes.c_uint32),
            ("hsv_enc", ctypes.c_uint32),
        ]

    _fields_ = [
        ("width", ctypes.c_uint32),
        ("height", ctypes.c_uint32),
        ("pixelformat", ctypes.c_uint32),
        ("field", ctypes.c_uint32),
        ("bytesperline", ctypes.c_uint32),
        ("sizeimage", ctypes.c_uint32),
        ("colorspace", ctypes.c_uint32),
        ("priv", ctypes.c_uint32),
        ("flags", ctypes.c_uint32),
        ("_", _encoding),
        ("quantization", ctypes.c_uint32),
        ("xfer_func", ctypes.c_uint32),
    ]

    _anonymous_ = ("_", )

    width = None
    height = None
    pixelformat = None
    field = None
    bytesperline = None
    sizeimage = None
    colorspace = None
    priv = None
    flags = None
    ycbcr_enc = None
    hsv_enc = None
    quantization = None
    xfer_func = None


class v4l2_rect(ctypes.Structure):
    _fields_ = [
        ("left", ctypes.c_int32),
        ("top", ctypes.c_int32),
        ("width", ctypes.c_uint32),
        ("height", ctypes.c_uint32),
    ]

    left = None
    top = None
    width = None
    height = None


class v4l2_clip(ctypes.Structure):
    c = None
    next = None


v4l2_clip._fields_ = [("c", v4l2_rect), ("next", ctypes.POINTER(v4l2_clip))]


class v4l2_window(ctypes.Structure):
    _fields_ = [
        ("w", v4l2_rect),
        ("field", ctypes.c_uint32),  # v4l2_field
        ("chromakey", ctypes.c_uint32),
        ("clips", ctypes.POINTER(v4l2_clip)),
        ("clipcount", ctypes.c_uint32),
        ("bitmap", ctypes.c_void_p),
        ("global_alpha", ctypes.c_uint8),
    ]

    w = None
    field = None
    chromakey = None
    clips = None
    clipcount = None
    bitmap = None
    global_alpha = None


class v4l2_vbi_format(ctypes.Structure):
    _fields_ = [
        ("sampling_rate", ctypes.c_uint32),  # in Hz
        ("offset", ctypes.c_uint32),
        ("samples_per_line", ctypes.c_uint32),
        ("sample_format", ctypes.c_uint32),  # V4L2_PIX_FMT_*
        ("start", ctypes.c_int32 * 2),
        ("count", ctypes.c_uint32 * 2),
        ("flags", ctypes.c_uint32),  # V4L2_VBI_*
        ("reserved", ctypes.c_uint32 * 2),
    ]

    sampling_rate = None
    offset = None
    samples_per_line = None
    sample_format = None
    start = None
    count = None
    flags = None
    reserved = None


class v4l2_sliced_vbi_format(ctypes.Structure):
    _fields_ = [
        ("service_set", ctypes.c_uint16),
        ("service_lines", ctypes.c_uint16 * 2 * 24),
        ("io_size", ctypes.c_uint32),
        ("reserved", ctypes.c_uint32),
    ]

    service_set = None
    service_lines = None
    io_size = None
    reserved = None


class v4l2_format(ctypes.Structure):

    class _fmt(ctypes.Union):
        _fields_ = [
            ("pix", v4l2_pix_format),
            ("win", v4l2_window),
            ("vbi", v4l2_vbi_format),
            ("sliced", v4l2_sliced_vbi_format),
            ("raw_data", ctypes.c_char * 200),
        ]

    _fields_ = [
        ("type", ctypes.c_uint32),  # v4l2_buf_type
        ("fmt", _fmt),
    ]

    type = None
    fmt = None


class v4l2_capability(ctypes.Structure):
    _fields_ = [
        ("driver", ctypes.c_char * 16),
        ("card", ctypes.c_char * 32),
        ("bus_info", ctypes.c_char * 32),
        ("version", ctypes.c_uint32),
        ("capabilities", ctypes.c_uint32),
        ("device_caps", ctypes.c_uint32),
        ("reserved", ctypes.c_uint32 * 3),
    ]

    driver = None
    card = None
    bus_info = None
    version = None
    capabilities = None
    device_caps = None
    reserved = None


class v4l2_fmtdesc(ctypes.Structure):
    _fields_ = [
        ("index", ctypes.c_uint32),
        ("type", ctypes.c_uint32),  # v4l2_buf_type
        ("flags", ctypes.c_uint32),
        ("description", ctypes.c_char * 32),  # Description string
        ("pixelformat", ctypes.c_uint32),  # Format fourcc
        ("mbus_code", ctypes.c_uint32),  # Media bus code
        ("reserved", ctypes.c_uint32 * 3),
    ]

    index = None
    type = None
    flags = None
    description = None
    pixelformat = None
    mbus_code = None
    reserved = None


class v4l2_control(ctypes.Structure):
    _fields_ = [
        ("id", ctypes.c_uint32),
        ("value", ctypes.c_int32),
    ]

    id = None
    value = None


class v4l2_ext_control(ctypes.Structure):

    class _anonymous(ctypes.Union):
        _fields_ = [
            ("value", ctypes.c_int32),
            ("value64", ctypes.c_int64),
            ("string", ctypes.c_char_p),
            ("p_u8", ctypes.POINTER(ctypes.c_uint8)),
            ("p_u16", ctypes.POINTER(ctypes.c_uint16)),
            ("p_u32", ctypes.POINTER(ctypes.c_uint32)),
            ("ptr", ctypes.c_void_p),
        ]

    _fields_ = [
        ("id", ctypes.c_uint32),
        ("size", ctypes.c_uint32),
        ("reserved2", ctypes.c_uint32),
        ("_", _anonymous),
    ]

    _anonymous_ = ("_", )
    _pack_ = 1

    id = None
    size = None
    reserved2 = None
    value = None
    value64 = None
    string = None
    p_u8 = None
    p_u16 = None
    p_u32 = None
    ptr = None


class v4l2_ext_controls(ctypes.Structure):

    class _anonymous(ctypes.Union):
        _fields_ = [
            ("ctrl_class", ctypes.c_uint32),
            ("which", ctypes.c_uint32),
        ]

    _fields_ = [
        ("_", _anonymous),
        ("count", ctypes.c_uint32),
        ("error_idx", ctypes.c_uint32),
        ("request_fd", ctypes.c_int32),
        ("reserved", ctypes.c_uint32),
        ("controls", ctypes.POINTER(v4l2_ext_control)),
    ]

    _anonymous_ = ("_", )

    ctrl_class = None
    which = None
    count = None
    error_idx = None
    request_fd = None
    reserved = None
    controls = None


class v4l2_frmsize_discrete(ctypes.Structure):
    _fields_ = [
        ("width", ctypes.c_uint32),  # Frame width [pixel]
        ("height", ctypes.c_uint32),  # Frame height [pixel]
    ]

    width = None
    height = None


class v4l2_frmsize_stepwise(ctypes.Structure):
    _fields_ = [
        ("min_width", ctypes.c_uint32),  # Minimum frame width [pixel]
        ("max_width", ctypes.c_uint32),  # Maximum frame width [pixel]
        ("step_width", ctypes.c_uint32),  # Frame width step size [pixel]
        ("min_height", ctypes.c_uint32),  # Minimum frame height [pixel]
        ("max_height", ctypes.c_uint32),  # Maximum frame height [pixel]
        ("step_height", ctypes.c_uint32),  # Frame height step size [pixel]
    ]

    min_width = None
    max_width = None
    step_width = None
    min_height = None
    max_height = None
    step_height = None


class v4l2_frmsizeenum(ctypes.Structure):

    class _anonymous(ctypes.Union):
        _fields_ = [
            ("discrete", v4l2_frmsize_discrete),
            ("stepwise", v4l2_frmsize_stepwise),
        ]

    _fields_ = [
        ("index", ctypes.c_uint32),  # Frame size number
        ("pixel_format", ctypes.c_uint32),  # Pixel format
        ("type", ctypes.c_uint32),  # Frame size type the device supports.
        ("_", _anonymous),  # Frame size
        ("reserved", ctypes.c_uint32 * 2),
    ]

    _anonymous_ = ("_", )

    index = None
    pixel_format = None
    type = None
    discrete = None
    stepwise = None
    reserved = None


# Used in the VIDIOC_QUERYCTRL ioctl for querying controls
class v4l2_queryctrl(ctypes.Structure):
    _fields_ = [
        ("id", ctypes.c_uint32),
        ("type", ctypes.c_uint32),  # v4l2_ctrl_type
        ("name", ctypes.c_char * 32),
        ("minimum", ctypes.c_int32),
        ("maximum", ctypes.c_int32),
        ("step", ctypes.c_int32),
        ("default_value", ctypes.c_int32),
        ("flags", ctypes.c_uint32),
        ("reserved", ctypes.c_uint32 * 2),
    ]

    id = None
    type = None
    name = None
    minimum = None
    maximum = None
    step = None
    default_value = None
    flags = None
    reserved = None


# Used in the VIDIOC_QUERY_EXT_CTRL ioctl for querying extended controls
class v4l2_query_ext_ctrl(ctypes.Structure):
    _fields_ = [
        ("id", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("name", ctypes.c_char * 32),
        ("minimum", ctypes.c_int64),
        ("maximum", ctypes.c_int64),
        ("step", ctypes.c_uint64),
        ("default_value", ctypes.c_int64),
        ("flags", ctypes.c_uint32),
        ("elem_size", ctypes.c_uint32),
        ("elems", ctypes.c_uint32),
        ("nr_of_dims", ctypes.c_uint32),
        ("dims", ctypes.c_uint32 * V4L2_CTRL_MAX_DIMS),
        ("reserved", ctypes.c_uint32 * 32),
    ]

    id = None
    type = None
    name = None
    minimum = None
    maximum = None
    step = None
    default_value = None
    flags = None
    elem_size = None
    elems = None
    nr_of_dims = None
    dims = None
    reserved = None


# Used in the VIDIOC_QUERYMENU ioctl for querying menu items
class v4l2_querymenu(ctypes.Structure):

    class _anonymous(ctypes.Union):
        _fields_ = [
            ("name", ctypes.c_char * 32),
            ("value", ctypes.c_int64),
        ]

    _fields_ = [
        ("id", ctypes.c_uint32),
        ("index", ctypes.c_uint32),
        ("_", _anonymous),
        ("reserved", ctypes.c_uint32),
    ]

    _anonymous_ = ("_", )
    _pack_ = 1

    id = None
    index = None
    name = None
    value = None
    reserved = None


class v4l2_requestbuffers(ctypes.Structure):
    _fields_ = [
        ("count", ctypes.c_uint32),
        ("type", ctypes.c_uint32),  # v4l2_buf_type
        ("memory", ctypes.c_uint32),  # v4l2_memory
        ("capabilities", ctypes.c_uint32),
        ("flags", ctypes.c_uint8),
        ("reserved", ctypes.c_uint8 * 3),
    ]

    count = None
    type = None
    memory = None
    capabilities = None
    flags = None
    reserved = None


class v4l2_plane(ctypes.Structure):

    class _m(ctypes.Union):
        _fields_ = [
            ("mem_offset", ctypes.c_uint32),
            ("userptr", ctypes.c_ulong),
            ("fd", ctypes.c_int32),
        ]

    _fields_ = [
        ("bytesused", ctypes.c_uint32),
        ("length", ctypes.c_uint32),
        ("m", _m),
        ("data_offset", ctypes.c_uint32),
        ("reserved", ctypes.c_uint32 * 11),
    ]

    bytesused = None
    length = None
    m = _m()
    data_offset = None
    reserved = None


class timeval(ctypes.Structure):
    _fields_ = [
        ("tv_sec", ctypes.c_long),
        ("tv_usec", ctypes.c_long),
    ]

    tv_sec = None
    tv_usec = None


class v4l2_timecode(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_uint32),
        ("flags", ctypes.c_uint32),
        ("frames", ctypes.c_uint8),
        ("seconds", ctypes.c_uint8),
        ("minutes", ctypes.c_uint8),
        ("hours", ctypes.c_uint8),
        ("userbits", ctypes.c_uint8 * 4),
    ]

    type = None
    flags = None
    frames = None
    seconds = None
    minutes = None
    hours = None
    userbits = None


class v4l2_buffer(ctypes.Structure):

    class _m(ctypes.Union):
        _fields_ = [
            ("offset", ctypes.c_uint32),
            ("userptr", ctypes.c_ulong),
            ("planes", ctypes.POINTER(v4l2_plane)),
            ("fd", ctypes.c_int32),
        ]

        offset = None
        userptr = None
        planes = None
        fd = None

    class _anonymous(ctypes.Union):
        _fields_ = [
            ("request_fd", ctypes.c_int32),
            ("reserved", ctypes.c_uint32),
        ]

    _fields_ = [
        ("index", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("bytesused", ctypes.c_uint32),
        ("flags", ctypes.c_uint32),
        ("field", ctypes.c_uint32),
        ("timestamp", timeval),
        ("timecode", v4l2_timecode),
        ("sequence", ctypes.c_uint32),
        ("memory", ctypes.c_uint32),
        ("m", _m),
        ("length", ctypes.c_uint32),
        ("reserved2", ctypes.c_uint32),
        ("_", _anonymous),
    ]

    _anonymous_ = ("_", )

    index = None
    type = None
    bytesused = None
    flags = None
    field = None
    timestamp = timeval()
    timecode = v4l2_timecode()
    sequence = None
    memory = None
    m = _m()
    length = None
    reserved2 = None
    request_fd = None
    reserved = None


class v4l2_fract(ctypes.Structure):
    _fields_ = [
        ("numerator", ctypes.c_uint32),
        ("denominator", ctypes.c_uint32),
    ]

    numerator = None
    denominator = None


class v4l2_captureparm(ctypes.Structure):
    _fields_ = [
        ("capability", ctypes.c_uint32),  # Supported modes
        ("capturemode", ctypes.c_uint32),  # Current mode
        ("timeperframe", v4l2_fract),  # Time per frame in seconds
        ("extendedmode", ctypes.c_uint32),  # Driver-specific extensions
        ("readbuffers", ctypes.c_uint32),  # # of buffers for read
        ("reserved", ctypes.c_uint32 * 4),
    ]

    capability = None
    capturemode = None
    timeperframe = v4l2_fract()
    extendedmode = None
    readbuffers = None
    reserved = None


class v4l2_outputparm(ctypes.Structure):
    _fields_ = [
        ("capability", ctypes.c_uint32),  # Supported modes
        ("outputmode", ctypes.c_uint32),  # Current mode
        ("timeperframe", v4l2_fract),  # Time per frame in seconds
        ("extendedmode", ctypes.c_uint32),  # Driver-specific extensions
        ("writebuffers", ctypes.c_uint32),  # # of buffers for read
        ("reserved", ctypes.c_uint32 * 4),
    ]

    capability = None
    outputmode = None
    timeperframe = v4l2_fract()
    extendedmode = None
    writebuffers = None
    reserved = None


class v4l2_streamparm(ctypes.Structure):

    class _parm(ctypes.Union):
        _fields_ = [
            ("capture", v4l2_captureparm),
            ("output", v4l2_outputparm),
            ("raw_data", ctypes.c_uint8 * 200),
        ]

        capture = v4l2_captureparm()
        output = v4l2_outputparm()
        raw_data = None

    _fields_ = [
        ("type", ctypes.c_uint32),  # v4l2_buf_type
        ("parm", _parm)
    ]

    type = None
    parm = _parm()


#
# ioctl codes
#
_IOC_NRBITS = 8
_IOC_TYPEBITS = 8
_IOC_SIZEBITS = 14

_IOC_NRSHIFT = 0
_IOC_TYPESHIFT = _IOC_NRSHIFT + _IOC_NRBITS
_IOC_SIZESHIFT = _IOC_TYPESHIFT + _IOC_TYPEBITS
_IOC_DIRSHIFT = _IOC_SIZESHIFT + _IOC_SIZEBITS

_IOC_WRITE = 1
_IOC_READ = 2


def _IOC(dir_, type_, nr, size):
    return (dir_ << _IOC_DIRSHIFT) | (ord(type_) << _IOC_TYPESHIFT) | (
        nr << _IOC_NRSHIFT) | (size << _IOC_SIZESHIFT)


def _IOC_TYPECHECK(t):
    return ctypes.sizeof(t)


def _IOR(type_, nr, size):
    return _IOC(_IOC_READ, type_, nr, _IOC_TYPECHECK(size))


def _IOW(type_, nr, size):
    return _IOC(_IOC_WRITE, type_, nr, _IOC_TYPECHECK(size))


def _IOWR(type_, nr, size):
    return _IOC(_IOC_READ | _IOC_WRITE, type_, nr, _IOC_TYPECHECK(size))


VIDIOC_QUERYCAP = _IOR('V', 0, v4l2_capability)
VIDIOC_ENUM_FMT = _IOWR('V', 2, v4l2_fmtdesc)
VIDIOC_G_FMT = _IOWR('V', 4, v4l2_format)
VIDIOC_S_FMT = _IOWR('V', 5, v4l2_format)
VIDIOC_REQBUFS = _IOWR('V', 8, v4l2_requestbuffers)
VIDIOC_QUERYBUF = _IOWR('V', 9, v4l2_buffer)
VIDIOC_QBUF = _IOWR('V', 15, v4l2_buffer)
VIDIOC_DQBUF = _IOWR('V', 17, v4l2_buffer)
VIDIOC_STREAMON = _IOW('V', 18, ctypes.c_int)
VIDIOC_STREAMOFF = _IOW('V', 19, ctypes.c_int)
VIDIOC_G_PARM = _IOWR('V', 21, v4l2_streamparm)
VIDIOC_S_PARM = _IOWR('V', 22, v4l2_streamparm)
VIDIOC_G_CTRL = _IOWR('V', 27, v4l2_control)
VIDIOC_S_CTRL = _IOWR('V', 28, v4l2_control)
VIDIOC_QUERYCTRL = _IOWR('V', 36, v4l2_queryctrl)
VIDIOC_QUERYMENU = _IOWR('V', 37, v4l2_querymenu)
VIDIOC_G_EXT_CTRLS = _IOWR('V', 71, v4l2_ext_controls)
VIDIOC_S_EXT_CTRLS = _IOWR('V', 72, v4l2_ext_controls)
VIDIOC_ENUM_FRAMESIZES = _IOWR('V', 74, v4l2_frmsizeenum)
VIDIOC_QUERY_EXT_CTRL = _IOWR('V', 103, v4l2_query_ext_ctrl)

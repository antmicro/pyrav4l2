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

V4L2_CAP_TIMEPERFRAME = 0x1000
V4L2_MODE_HIGHQUALITY = 0x0001

V4L2_FRMIVAL_TYPE_DISCRETE = 1
V4L2_FRMIVAL_TYPE_CONTINUOUS = 2
V4L2_FRMIVAL_TYPE_STEPWISE = 3


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


# Pixel format FOURCC


#  Four-character-code (FOURCC)
def v4l2_fourcc(a, b, c, d):
    return ord(a) | (ord(b) << 8) | (ord(c) << 16) | (ord(d) << 24)


def v4l2_fourcc_be(a, b, c, d):
    return v4l2_fourcc(a, b, c, d) | (1 << 31)


# RGB formats (1 or 2 bytes per pixel)
V4L2_PIX_FMT_RGB332 = v4l2_fourcc('R', 'G', 'B', '1')  #  8  RGB-3-3-2
V4L2_PIX_FMT_RGB444 = v4l2_fourcc('R', '4', '4', '4')  # 16  xxxxrrrr ggggbbbb
V4L2_PIX_FMT_ARGB444 = v4l2_fourcc('A', 'R', '1', '2')  # 16  aaaarrrr ggggbbbb
V4L2_PIX_FMT_XRGB444 = v4l2_fourcc('X', 'R', '1', '2')  # 16  xxxxrrrr ggggbbbb
V4L2_PIX_FMT_RGBA444 = v4l2_fourcc('R', 'A', '1', '2')  # 16  rrrrgggg bbbbaaaa
V4L2_PIX_FMT_RGBX444 = v4l2_fourcc('R', 'X', '1', '2')  # 16  rrrrgggg bbbbxxxx
V4L2_PIX_FMT_ABGR444 = v4l2_fourcc('A', 'B', '1', '2')  # 16  aaaabbbb ggggrrrr
V4L2_PIX_FMT_XBGR444 = v4l2_fourcc('X', 'B', '1', '2')  # 16  xxxxbbbb ggggrrrr
V4L2_PIX_FMT_BGRA444 = v4l2_fourcc('G', 'A', '1', '2')  # 16  bbbbgggg rrrraaaa
V4L2_PIX_FMT_BGRX444 = v4l2_fourcc('B', 'X', '1', '2')  # 16  bbbbgggg rrrrxxxx
V4L2_PIX_FMT_RGB555 = v4l2_fourcc('R', 'G', 'B', 'O')  # 16  RGB-5-5-5
V4L2_PIX_FMT_ARGB555 = v4l2_fourcc('A', 'R', '1', '5')  # 16  ARGB-1-5-5-5
V4L2_PIX_FMT_XRGB555 = v4l2_fourcc('X', 'R', '1', '5')  # 16  XRGB-1-5-5-5
V4L2_PIX_FMT_RGBA555 = v4l2_fourcc('R', 'A', '1', '5')  # 16  RGBA-5-5-5-1
V4L2_PIX_FMT_RGBX555 = v4l2_fourcc('R', 'X', '1', '5')  # 16  RGBX-5-5-5-1
V4L2_PIX_FMT_ABGR555 = v4l2_fourcc('A', 'B', '1', '5')  # 16  ABGR-1-5-5-5
V4L2_PIX_FMT_XBGR555 = v4l2_fourcc('X', 'B', '1', '5')  # 16  XBGR-1-5-5-5
V4L2_PIX_FMT_BGRA555 = v4l2_fourcc('B', 'A', '1', '5')  # 16  BGRA-5-5-5-1
V4L2_PIX_FMT_BGRX555 = v4l2_fourcc('B', 'X', '1', '5')  # 16  BGRX-5-5-5-1
V4L2_PIX_FMT_RGB565 = v4l2_fourcc('R', 'G', 'B', 'P')  # 16  RGB-5-6-5
V4L2_PIX_FMT_RGB555X = v4l2_fourcc('R', 'G', 'B', 'Q')  # 16  RGB-5-5-5 BE
V4L2_PIX_FMT_ARGB555X = v4l2_fourcc_be('A', 'R', '1', '5')  # 16  ARGB-5-5-5 BE
V4L2_PIX_FMT_XRGB555X = v4l2_fourcc_be('X', 'R', '1', '5')  # 16  XRGB-5-5-5 BE
V4L2_PIX_FMT_RGB565X = v4l2_fourcc('R', 'G', 'B', 'R')  # 16  RGB-5-6-5 BE

# RGB formats (3 or 4 bytes per pixel)
V4L2_PIX_FMT_BGR666 = v4l2_fourcc('B', 'G', 'R', 'H')  # 18  BGR-6-6-6
V4L2_PIX_FMT_BGR24 = v4l2_fourcc('B', 'G', 'R', '3')  # 24  BGR-8-8-8
V4L2_PIX_FMT_RGB24 = v4l2_fourcc('R', 'G', 'B', '3')  # 24  RGB-8-8-8
V4L2_PIX_FMT_BGR32 = v4l2_fourcc('B', 'G', 'R', '4')  # 32  BGR-8-8-8-8
V4L2_PIX_FMT_ABGR32 = v4l2_fourcc('A', 'R', '2', '4')  # 32  BGRA-8-8-8-8
V4L2_PIX_FMT_XBGR32 = v4l2_fourcc('X', 'R', '2', '4')  # 32  BGRX-8-8-8-8
V4L2_PIX_FMT_BGRA32 = v4l2_fourcc('R', 'A', '2', '4')  # 32  ABGR-8-8-8-8
V4L2_PIX_FMT_BGRX32 = v4l2_fourcc('R', 'X', '2', '4')  # 32  XBGR-8-8-8-8
V4L2_PIX_FMT_RGB32 = v4l2_fourcc('R', 'G', 'B', '4')  # 32  RGB-8-8-8-8
V4L2_PIX_FMT_RGBA32 = v4l2_fourcc('A', 'B', '2', '4')  # 32  RGBA-8-8-8-8
V4L2_PIX_FMT_RGBX32 = v4l2_fourcc('X', 'B', '2', '4')  # 32  RGBX-8-8-8-8
V4L2_PIX_FMT_ARGB32 = v4l2_fourcc('B', 'A', '2', '4')  # 32  ARGB-8-8-8-8
V4L2_PIX_FMT_XRGB32 = v4l2_fourcc('B', 'X', '2', '4')  # 32  XRGB-8-8-8-8

# Grey formats
V4L2_PIX_FMT_GREY = v4l2_fourcc('G', 'R', 'E', 'Y')  #  8  Greyscale
V4L2_PIX_FMT_Y4 = v4l2_fourcc('Y', '0', '4', ' ')  #  4  Greyscale
V4L2_PIX_FMT_Y6 = v4l2_fourcc('Y', '0', '6', ' ')  #  6  Greyscale
V4L2_PIX_FMT_Y10 = v4l2_fourcc('Y', '1', '0', ' ')  # 10  Greyscale
V4L2_PIX_FMT_Y12 = v4l2_fourcc('Y', '1', '2', ' ')  # 12  Greyscale
V4L2_PIX_FMT_Y14 = v4l2_fourcc('Y', '1', '4', ' ')  # 14  Greyscale
V4L2_PIX_FMT_Y16 = v4l2_fourcc('Y', '1', '6', ' ')  # 16  Greyscale
V4L2_PIX_FMT_Y16_BE = v4l2_fourcc_be('Y', '1', '6', ' ')  # 16  Greyscale BE

# Grey bit-packed formats
V4L2_PIX_FMT_Y10BPACK = v4l2_fourcc('Y', '1', '0',
                                    'B')  # 10  Greyscale bit-packed
V4L2_PIX_FMT_Y10P = v4l2_fourcc('Y', '1', '0',
                                'P')  # 10  Greyscale, MIPI RAW10 packed

# Palette formats
V4L2_PIX_FMT_PAL8 = v4l2_fourcc('P', 'A', 'L', '8')  #  8  8-bit palette

# Chrominance formats
V4L2_PIX_FMT_UV8 = v4l2_fourcc('U', 'V', '8', ' ')  #  8  UV 4:4

# Luminance+Chrominance formats
V4L2_PIX_FMT_YUYV = v4l2_fourcc('Y', 'U', 'Y', 'V')  # 16  YUV 4:2:2
V4L2_PIX_FMT_YYUV = v4l2_fourcc('Y', 'Y', 'U', 'V')  # 16  YUV 4:2:2
V4L2_PIX_FMT_YVYU = v4l2_fourcc('Y', 'V', 'Y', 'U')  # 16 YVU 4:2:2
V4L2_PIX_FMT_UYVY = v4l2_fourcc('U', 'Y', 'V', 'Y')  # 16  YUV 4:2:2
V4L2_PIX_FMT_VYUY = v4l2_fourcc('V', 'Y', 'U', 'Y')  # 16  YUV 4:2:2
V4L2_PIX_FMT_Y41P = v4l2_fourcc('Y', '4', '1', 'P')  # 12  YUV 4:1:1
V4L2_PIX_FMT_YUV444 = v4l2_fourcc('Y', '4', '4', '4')  # 16  xxxxyyyy uuuuvvvv
V4L2_PIX_FMT_YUV555 = v4l2_fourcc('Y', 'U', 'V', 'O')  # 16  YUV-5-5-5
V4L2_PIX_FMT_YUV565 = v4l2_fourcc('Y', 'U', 'V', 'P')  # 16  YUV-5-6-5
V4L2_PIX_FMT_YUV24 = v4l2_fourcc('Y', 'U', 'V', '3')  # 24  YUV-8-8-8
V4L2_PIX_FMT_YUV32 = v4l2_fourcc('Y', 'U', 'V', '4')  # 32  YUV-8-8-8-8
V4L2_PIX_FMT_AYUV32 = v4l2_fourcc('A', 'Y', 'U', 'V')  # 32  AYUV-8-8-8-8
V4L2_PIX_FMT_XYUV32 = v4l2_fourcc('X', 'Y', 'U', 'V')  # 32  XYUV-8-8-8-8
V4L2_PIX_FMT_VUYA32 = v4l2_fourcc('V', 'U', 'Y', 'A')  # 32  VUYA-8-8-8-8
V4L2_PIX_FMT_VUYX32 = v4l2_fourcc('V', 'U', 'Y', 'X')  # 32  VUYX-8-8-8-8
V4L2_PIX_FMT_M420 = v4l2_fourcc(
    'M', '4', '2', '0')  # 12  YUV 4:2:0 2 lines y, 1 line uv interleaved

# two planes -- one Y, one Cr + Cb interleaved
V4L2_PIX_FMT_NV12 = v4l2_fourcc('N', 'V', '1', '2')  # 12  Y/CbCr 4:2:0
V4L2_PIX_FMT_NV21 = v4l2_fourcc('N', 'V', '2', '1')  # 12  Y/CrCb 4:2:0
V4L2_PIX_FMT_NV16 = v4l2_fourcc('N', 'V', '1', '6')  # 16  Y/CbCr 4:2:2
V4L2_PIX_FMT_NV61 = v4l2_fourcc('N', 'V', '6', '1')  # 16  Y/CrCb 4:2:2
V4L2_PIX_FMT_NV24 = v4l2_fourcc('N', 'V', '2', '4')  # 24  Y/CbCr 4:4:4
V4L2_PIX_FMT_NV42 = v4l2_fourcc('N', 'V', '4', '2')  # 24  Y/CrCb 4:4:4

# two non contiguous planes - one Y, one Cr + Cb interleaved
V4L2_PIX_FMT_NV12M = v4l2_fourcc('N', 'M', '1', '2')  # 12  Y/CbCr 4:2:0
V4L2_PIX_FMT_NV21M = v4l2_fourcc('N', 'M', '2', '1')  # 21  Y/CrCb 4:2:0
V4L2_PIX_FMT_NV16M = v4l2_fourcc('N', 'M', '1', '6')  # 16  Y/CbCr 4:2:2
V4L2_PIX_FMT_NV61M = v4l2_fourcc('N', 'M', '6', '1')  # 16  Y/CrCb 4:2:2

# three planes - Y Cb, Cr
V4L2_PIX_FMT_YUV410 = v4l2_fourcc('Y', 'U', 'V', '9')  #  9  YUV 4:1:0
V4L2_PIX_FMT_YVU410 = v4l2_fourcc('Y', 'V', 'U', '9')  #  9  YVU 4:1:0
V4L2_PIX_FMT_YUV411P = v4l2_fourcc('4', '1', '1', 'P')  # 12  YVU411 planar
V4L2_PIX_FMT_YUV420 = v4l2_fourcc('Y', 'U', '1', '2')  # 12  YUV 4:2:0
V4L2_PIX_FMT_YVU420 = v4l2_fourcc('Y', 'V', '1', '2')  # 12  YVU 4:2:0
V4L2_PIX_FMT_YUV422P = v4l2_fourcc('4', '2', '2', 'P')  # 16  YVU422 planar

# three non contiguous planes - Y, Cb, Cr
V4L2_PIX_FMT_YUV420M = v4l2_fourcc('Y', 'M', '1', '2')  # 12  YUV420 planar
V4L2_PIX_FMT_YVU420M = v4l2_fourcc('Y', 'M', '2', '1')  # 12  YVU420 planar
V4L2_PIX_FMT_YUV422M = v4l2_fourcc('Y', 'M', '1', '6')  # 16  YUV422 planar
V4L2_PIX_FMT_YVU422M = v4l2_fourcc('Y', 'M', '6', '1')  # 16  YVU422 planar
V4L2_PIX_FMT_YUV444M = v4l2_fourcc('Y', 'M', '2', '4')  # 24  YUV444 planar
V4L2_PIX_FMT_YVU444M = v4l2_fourcc('Y', 'M', '4', '2')  # 24  YVU444 planar

# Tiled YUV formats
V4L2_PIX_FMT_NV12_4L4 = v4l2_fourcc('V', 'T', '1',
                                    '2')  # 12  Y/CbCr 4:2:0  4x4 tiles
V4L2_PIX_FMT_NV12_16L16 = v4l2_fourcc('H', 'M', '1',
                                      '2')  # 12  Y/CbCr 4:2:0 16x16 tiles
V4L2_PIX_FMT_NV12_32L32 = v4l2_fourcc('S', 'T', '1',
                                      '2')  # 12  Y/CbCr 4:2:0 32x32 tiles

# Tiled YUV formats, non contiguous planes
V4L2_PIX_FMT_NV12MT = v4l2_fourcc('T', 'M', '1',
                                  '2')  # 12  Y/CbCr 4:2:0 64x32 tiles
V4L2_PIX_FMT_NV12MT_16X16 = v4l2_fourcc('V', 'M', '1',
                                        '2')  # 12  Y/CbCr 4:2:0 16x16 tiles
V4L2_PIX_FMT_NV12M_8L128 = v4l2_fourcc('N', 'A', '1',
                                       '2')  # Y/CbCr 4:2:0 8x128 tiles
V4L2_PIX_FMT_NV12M_10BE_8L128 = v4l2_fourcc_be(
    'N', 'T', '1', '2')  # Y/CbCr 4:2:0 10-bit 8x128 tiles

# Bayer formats - see http://www.siliconimaging.com/RGB%20Bayer.htm
V4L2_PIX_FMT_SBGGR8 = v4l2_fourcc('B', 'A', '8', '1')  #  8  BGBG.. GRGR..
V4L2_PIX_FMT_SGBRG8 = v4l2_fourcc('G', 'B', 'R', 'G')  #  8  GBGB.. RGRG..
V4L2_PIX_FMT_SGRBG8 = v4l2_fourcc('G', 'R', 'B', 'G')  #  8  GRGR.. BGBG..
V4L2_PIX_FMT_SRGGB8 = v4l2_fourcc('R', 'G', 'G', 'B')  #  8  RGRG.. GBGB..
V4L2_PIX_FMT_SBGGR10 = v4l2_fourcc('B', 'G', '1', '0')  # 10  BGBG.. GRGR..
V4L2_PIX_FMT_SGBRG10 = v4l2_fourcc('G', 'B', '1', '0')  # 10  GBGB.. RGRG..
V4L2_PIX_FMT_SGRBG10 = v4l2_fourcc('B', 'A', '1', '0')  # 10  GRGR.. BGBG..
V4L2_PIX_FMT_SRGGB10 = v4l2_fourcc('R', 'G', '1', '0')  # 10  RGRG.. GBGB..
# 10bit raw bayer packed, 5 bytes for every 4 pixels
V4L2_PIX_FMT_SBGGR10P = v4l2_fourcc('p', 'B', 'A', 'A')
V4L2_PIX_FMT_SGBRG10P = v4l2_fourcc('p', 'G', 'A', 'A')
V4L2_PIX_FMT_SGRBG10P = v4l2_fourcc('p', 'g', 'A', 'A')
V4L2_PIX_FMT_SRGGB10P = v4l2_fourcc('p', 'R', 'A', 'A')
# 10bit raw bayer a-law compressed to 8 bits
V4L2_PIX_FMT_SBGGR10ALAW8 = v4l2_fourcc('a', 'B', 'A', '8')
V4L2_PIX_FMT_SGBRG10ALAW8 = v4l2_fourcc('a', 'G', 'A', '8')
V4L2_PIX_FMT_SGRBG10ALAW8 = v4l2_fourcc('a', 'g', 'A', '8')
V4L2_PIX_FMT_SRGGB10ALAW8 = v4l2_fourcc('a', 'R', 'A', '8')
# 10bit raw bayer DPCM compressed to 8 bits
V4L2_PIX_FMT_SBGGR10DPCM8 = v4l2_fourcc('b', 'B', 'A', '8')
V4L2_PIX_FMT_SGBRG10DPCM8 = v4l2_fourcc('b', 'G', 'A', '8')
V4L2_PIX_FMT_SGRBG10DPCM8 = v4l2_fourcc('B', 'D', '1', '0')
V4L2_PIX_FMT_SRGGB10DPCM8 = v4l2_fourcc('b', 'R', 'A', '8')
V4L2_PIX_FMT_SBGGR12 = v4l2_fourcc('B', 'G', '1', '2')  # 12  BGBG.. GRGR..
V4L2_PIX_FMT_SGBRG12 = v4l2_fourcc('G', 'B', '1', '2')  # 12  GBGB.. RGRG..
V4L2_PIX_FMT_SGRBG12 = v4l2_fourcc('B', 'A', '1', '2')  # 12  GRGR.. BGBG..
V4L2_PIX_FMT_SRGGB12 = v4l2_fourcc('R', 'G', '1', '2')  # 12  RGRG.. GBGB..
# 12bit raw bayer packed, 6 bytes for every 4 pixels
V4L2_PIX_FMT_SBGGR12P = v4l2_fourcc('p', 'B', 'C', 'C')
V4L2_PIX_FMT_SGBRG12P = v4l2_fourcc('p', 'G', 'C', 'C')
V4L2_PIX_FMT_SGRBG12P = v4l2_fourcc('p', 'g', 'C', 'C')
V4L2_PIX_FMT_SRGGB12P = v4l2_fourcc('p', 'R', 'C', 'C')
V4L2_PIX_FMT_SBGGR14 = v4l2_fourcc('B', 'G', '1', '4')  # 14  BGBG.. GRGR..
V4L2_PIX_FMT_SGBRG14 = v4l2_fourcc('G', 'B', '1', '4')  # 14  GBGB.. RGRG..
V4L2_PIX_FMT_SGRBG14 = v4l2_fourcc('G', 'R', '1', '4')  # 14  GRGR.. BGBG..
V4L2_PIX_FMT_SRGGB14 = v4l2_fourcc('R', 'G', '1', '4')  # 14  RGRG.. GBGB..
# 14bit raw bayer packed, 7 bytes for every 4 pixels
V4L2_PIX_FMT_SBGGR14P = v4l2_fourcc('p', 'B', 'E', 'E')
V4L2_PIX_FMT_SGBRG14P = v4l2_fourcc('p', 'G', 'E', 'E')
V4L2_PIX_FMT_SGRBG14P = v4l2_fourcc('p', 'g', 'E', 'E')
V4L2_PIX_FMT_SRGGB14P = v4l2_fourcc('p', 'R', 'E', 'E')
V4L2_PIX_FMT_SBGGR16 = v4l2_fourcc('B', 'Y', 'R', '2')  # 16  BGBG.. GRGR..
V4L2_PIX_FMT_SGBRG16 = v4l2_fourcc('G', 'B', '1', '6')  # 16  GBGB.. RGRG..
V4L2_PIX_FMT_SGRBG16 = v4l2_fourcc('G', 'R', '1', '6')  # 16  GRGR.. BGBG..
V4L2_PIX_FMT_SRGGB16 = v4l2_fourcc('R', 'G', '1', '6')  # 16  RGRG.. GBGB..

# HSV formats
V4L2_PIX_FMT_HSV24 = v4l2_fourcc('H', 'S', 'V', '3')
V4L2_PIX_FMT_HSV32 = v4l2_fourcc('H', 'S', 'V', '4')

# compressed formats
V4L2_PIX_FMT_MJPEG = v4l2_fourcc('M', 'J', 'P', 'G')  # Motion-JPEG
V4L2_PIX_FMT_JPEG = v4l2_fourcc('J', 'P', 'E', 'G')  # JFIF JPEG
V4L2_PIX_FMT_DV = v4l2_fourcc('d', 'v', 's', 'd')  # 1394
V4L2_PIX_FMT_MPEG = v4l2_fourcc('M', 'P', 'E', 'G')  # MPEG-1/2/4 Multiplexed
V4L2_PIX_FMT_H264 = v4l2_fourcc('H', '2', '6', '4')  # H264 with start codes
V4L2_PIX_FMT_H264_NO_SC = v4l2_fourcc('A', 'V', 'C',
                                      '1')  # H264 without start codes
V4L2_PIX_FMT_H264_MVC = v4l2_fourcc('M', '2', '6', '4')  # H264 MVC
V4L2_PIX_FMT_H263 = v4l2_fourcc('H', '2', '6', '3')  # H263
V4L2_PIX_FMT_MPEG1 = v4l2_fourcc('M', 'P', 'G', '1')  # MPEG-1 ES
V4L2_PIX_FMT_MPEG2 = v4l2_fourcc('M', 'P', 'G', '2')  # MPEG-2 ES
V4L2_PIX_FMT_MPEG2_SLICE = v4l2_fourcc('M', 'G', '2',
                                       'S')  # MPEG-2 parsed slice data
V4L2_PIX_FMT_MPEG4 = v4l2_fourcc('M', 'P', 'G', '4')  # MPEG-4 part 2 ES
V4L2_PIX_FMT_XVID = v4l2_fourcc('X', 'V', 'I', 'D')  # Xvid
V4L2_PIX_FMT_VC1_ANNEX_G = v4l2_fourcc(
    'V', 'C', '1', 'G')  # SMPTE 421M Annex G compliant stream
V4L2_PIX_FMT_VC1_ANNEX_L = v4l2_fourcc(
    'V', 'C', '1', 'L')  # SMPTE 421M Annex L compliant stream
V4L2_PIX_FMT_VP8 = v4l2_fourcc('V', 'P', '8', '0')  # VP8
V4L2_PIX_FMT_VP8_FRAME = v4l2_fourcc('V', 'P', '8', 'F')  # VP8 parsed frame
V4L2_PIX_FMT_VP9 = v4l2_fourcc('V', 'P', '9', '0')  # VP9
V4L2_PIX_FMT_VP9_FRAME = v4l2_fourcc('V', 'P', '9', 'F')  # VP9 parsed frame
V4L2_PIX_FMT_HEVC = v4l2_fourcc('H', 'E', 'V', 'C')  # HEVC aka H.265
V4L2_PIX_FMT_FWHT = v4l2_fourcc('F', 'W', 'H',
                                'T')  # Fast Walsh Hadamard Transform (vicodec)
V4L2_PIX_FMT_FWHT_STATELESS = v4l2_fourcc('S', 'F', 'W',
                                          'H')  # Stateless FWHT (vicodec)
V4L2_PIX_FMT_H264_SLICE = v4l2_fourcc('S', '2', '6', '4')  # H264 parsed slices

#  Vendor-specific formats
V4L2_PIX_FMT_CPIA1 = v4l2_fourcc('C', 'P', 'I', 'A')  # cpia1 YUV
V4L2_PIX_FMT_WNVA = v4l2_fourcc('W', 'N', 'V', 'A')  # Winnov hw compress
V4L2_PIX_FMT_SN9C10X = v4l2_fourcc('S', '9', '1', '0')  # SN9C10x compression
V4L2_PIX_FMT_SN9C20X_I420 = v4l2_fourcc('S', '9', '2',
                                        '0')  # SN9C20x YUV 4:2:0
V4L2_PIX_FMT_PWC1 = v4l2_fourcc('P', 'W', 'C', '1')  # pwc older webcam
V4L2_PIX_FMT_PWC2 = v4l2_fourcc('P', 'W', 'C', '2')  # pwc newer webcam
V4L2_PIX_FMT_ET61X251 = v4l2_fourcc('E', '6', '2', '5')  # ET61X251 compression
V4L2_PIX_FMT_SPCA501 = v4l2_fourcc('S', '5', '0', '1')  # YUYV per line
V4L2_PIX_FMT_SPCA505 = v4l2_fourcc('S', '5', '0', '5')  # YYUV per line
V4L2_PIX_FMT_SPCA508 = v4l2_fourcc('S', '5', '0', '8')  # YUVY per line
V4L2_PIX_FMT_SPCA561 = v4l2_fourcc('S', '5', '6', '1')  # compressed GBRG bayer
V4L2_PIX_FMT_PAC207 = v4l2_fourcc('P', '2', '0', '7')  # compressed BGGR bayer
V4L2_PIX_FMT_MR97310A = v4l2_fourcc('M', '3', '1',
                                    '0')  # compressed BGGR bayer
V4L2_PIX_FMT_JL2005BCD = v4l2_fourcc('J', 'L', '2',
                                     '0')  # compressed RGGB bayer
V4L2_PIX_FMT_SN9C2028 = v4l2_fourcc('S', 'O', 'N',
                                    'X')  # compressed GBRG bayer
V4L2_PIX_FMT_SQ905C = v4l2_fourcc('9', '0', '5', 'C')  # compressed RGGB bayer
V4L2_PIX_FMT_PJPG = v4l2_fourcc('P', 'J', 'P', 'G')  # Pixart 73xx JPEG
V4L2_PIX_FMT_OV511 = v4l2_fourcc('O', '5', '1', '1')  # ov511 JPEG
V4L2_PIX_FMT_OV518 = v4l2_fourcc('O', '5', '1', '8')  # ov518 JPEG
V4L2_PIX_FMT_STV0680 = v4l2_fourcc('S', '6', '8', '0')  # stv0680 bayer
V4L2_PIX_FMT_TM6000 = v4l2_fourcc('T', 'M', '6', '0')  # tm5600/tm60x0
V4L2_PIX_FMT_CIT_YYVYUY = v4l2_fourcc('C', 'I', 'T',
                                      'V')  # one line of Y then 1 line of VYUY
V4L2_PIX_FMT_KONICA420 = v4l2_fourcc(
    'K', 'O', 'N', 'I')  # YUV420 planar in blocks of 256 pixels
V4L2_PIX_FMT_JPGL = v4l2_fourcc('J', 'P', 'G', 'L')  # JPEG-Lite
V4L2_PIX_FMT_SE401 = v4l2_fourcc('S', '4', '0',
                                 '1')  # se401 janggu compressed rgb
V4L2_PIX_FMT_S5C_UYVY_JPG = v4l2_fourcc('S', '5', 'C',
                                        'I')  # S5C73M3 interleaved UYVY/JPEG
V4L2_PIX_FMT_Y8I = v4l2_fourcc('Y', '8', 'I',
                               ' ')  # Greyscale 8-bit L/R interleaved
V4L2_PIX_FMT_Y12I = v4l2_fourcc('Y', '1', '2',
                                'I')  # Greyscale 12-bit L/R interleaved
V4L2_PIX_FMT_Z16 = v4l2_fourcc('Z', '1', '6', ' ')  # Depth data 16-bit
V4L2_PIX_FMT_MT21C = v4l2_fourcc('M', 'T', '2',
                                 '1')  # Mediatek compressed block mode
V4L2_PIX_FMT_MM21 = v4l2_fourcc(
    'M', 'M', '2', '1')  # Mediatek 8-bit block mode, two non-contiguous planes
V4L2_PIX_FMT_INZI = v4l2_fourcc(
    'I', 'N', 'Z', 'I')  # Intel Planar Greyscale 10-bit and Depth 16-bit
V4L2_PIX_FMT_CNF4 = v4l2_fourcc(
    'C', 'N', 'F', '4')  # Intel 4-bit packed depth confidence information
V4L2_PIX_FMT_HI240 = v4l2_fourcc('H', 'I', '2', '4')  # BTTV 8-bit dithered RGB

# 10bit raw bayer packed, 32 bytes for every 25 pixels, last LSB 6 bits unused
V4L2_PIX_FMT_IPU3_SBGGR10 = v4l2_fourcc('i', 'p', '3',
                                        'b')  # IPU3 packed 10-bit BGGR bayer
V4L2_PIX_FMT_IPU3_SGBRG10 = v4l2_fourcc('i', 'p', '3',
                                        'g')  # IPU3 packed 10-bit GBRG bayer
V4L2_PIX_FMT_IPU3_SGRBG10 = v4l2_fourcc('i', 'p', '3',
                                        'G')  # IPU3 packed 10-bit GRBG bayer
V4L2_PIX_FMT_IPU3_SRGGB10 = v4l2_fourcc('i', 'p', '3',
                                        'r')  # IPU3 packed 10-bit RGGB bayer


class v4l2_frmival_stepwise(ctypes.Structure):
    _fields_ = [
        ("min", v4l2_fract),
        ("max", v4l2_fract),
        ("step", v4l2_fract),
    ]

    min = v4l2_fract()
    max = v4l2_fract()
    step = v4l2_fract()


class v4l2_frmivalenum(ctypes.Structure):

    class _anonymous(ctypes.Union):
        _fields_ = [
            ("discrete", v4l2_fract),
            ("stepwise", v4l2_frmival_stepwise),
        ]

    _fields_ = [
        ("index", ctypes.c_uint32),
        ("pixel_format", ctypes.c_uint32),
        ("width", ctypes.c_uint32),
        ("height", ctypes.c_uint32),
        ("type", ctypes.c_uint32),
        ("_", _anonymous),
        ("reserved", ctypes.c_uint32 * 2),
    ]

    _anonymous_ = ("_", )

    index = None
    pixel_format = None
    width = None
    height = None
    type = None
    discrete = v4l2_fract()
    stepwise = v4l2_frmival_stepwise()
    reserved = None


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
VIDIOC_ENUM_FRAMEINTERVALS = _IOWR('V', 75, v4l2_frmivalenum)
VIDIOC_QUERY_EXT_CTRL = _IOWR('V', 103, v4l2_query_ext_ctrl)

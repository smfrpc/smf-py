# automatically generated by the FlatBuffers compiler, do not modify

# namespace: rpc

import flatbuffers

# /// \brief used for extra headers, ala HTTP
# /// The use case for the core is to support
# /// zipkin/google-Dapper style tracing
class dynamic_header(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsdynamic_header(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = dynamic_header()
        x.Init(buf, n + offset)
        return x

    # dynamic_header
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

# /// alows for binary search lookup
# /// use with CreateVectorOfSortedTables<> instead of the CreateVector
    # dynamic_header
    def Key(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # dynamic_header
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def dynamic_headerStart(builder): builder.StartObject(2)
def dynamic_headerAddKey(builder, key): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(key), 0)
def dynamic_headerAddValue(builder, value): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def dynamic_headerEnd(builder): return builder.EndObject()

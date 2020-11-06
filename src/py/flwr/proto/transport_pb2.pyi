# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    NewType as typing___NewType,
    Optional as typing___Optional,
    Text as typing___Text,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

ReasonValue = typing___NewType('ReasonValue', builtin___int)
type___ReasonValue = ReasonValue
Reason: _Reason
class _Reason(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[ReasonValue]):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    UNKNOWN = typing___cast(ReasonValue, 0)
    RECONNECT = typing___cast(ReasonValue, 1)
    POWER_DISCONNECTED = typing___cast(ReasonValue, 2)
    WIFI_UNAVAILABLE = typing___cast(ReasonValue, 3)
    ACK = typing___cast(ReasonValue, 4)
UNKNOWN = typing___cast(ReasonValue, 0)
RECONNECT = typing___cast(ReasonValue, 1)
POWER_DISCONNECTED = typing___cast(ReasonValue, 2)
WIFI_UNAVAILABLE = typing___cast(ReasonValue, 3)
ACK = typing___cast(ReasonValue, 4)
type___Reason = Reason

class Parameters(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    tensors: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___bytes] = ...
    tensor_type: typing___Text = ...

    def __init__(self,
        *,
        tensors : typing___Optional[typing___Iterable[builtin___bytes]] = None,
        tensor_type : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"tensor_type",b"tensor_type",u"tensors",b"tensors"]) -> None: ...
type___Parameters = Parameters

class ServerMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Reconnect(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        seconds: builtin___int = ...

        def __init__(self,
            *,
            seconds : typing___Optional[builtin___int] = None,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"seconds",b"seconds"]) -> None: ...
    type___Reconnect = Reconnect

    class GetParameters(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        def __init__(self,
            ) -> None: ...
    type___GetParameters = GetParameters

    class FitIns(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class ConfigEntry(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            key: typing___Text = ...
            value: typing___Text = ...

            def __init__(self,
                *,
                key : typing___Optional[typing___Text] = None,
                value : typing___Optional[typing___Text] = None,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
        type___ConfigEntry = ConfigEntry


        @property
        def parameters(self) -> type___Parameters: ...

        @property
        def config(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...

        def __init__(self,
            *,
            parameters : typing___Optional[type___Parameters] = None,
            config : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"parameters",b"parameters"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"config",b"config",u"parameters",b"parameters"]) -> None: ...
    type___FitIns = FitIns

    class EvaluateIns(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class ConfigEntry(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            key: typing___Text = ...
            value: typing___Text = ...

            def __init__(self,
                *,
                key : typing___Optional[typing___Text] = None,
                value : typing___Optional[typing___Text] = None,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
        type___ConfigEntry = ConfigEntry


        @property
        def parameters(self) -> type___Parameters: ...

        @property
        def config(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...

        def __init__(self,
            *,
            parameters : typing___Optional[type___Parameters] = None,
            config : typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"parameters",b"parameters"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"config",b"config",u"parameters",b"parameters"]) -> None: ...
    type___EvaluateIns = EvaluateIns


    @property
    def reconnect(self) -> type___ServerMessage.Reconnect: ...

    @property
    def get_parameters(self) -> type___ServerMessage.GetParameters: ...

    @property
    def fit_ins(self) -> type___ServerMessage.FitIns: ...

    @property
    def evaluate_ins(self) -> type___ServerMessage.EvaluateIns: ...

    def __init__(self,
        *,
        reconnect : typing___Optional[type___ServerMessage.Reconnect] = None,
        get_parameters : typing___Optional[type___ServerMessage.GetParameters] = None,
        fit_ins : typing___Optional[type___ServerMessage.FitIns] = None,
        evaluate_ins : typing___Optional[type___ServerMessage.EvaluateIns] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"evaluate_ins",b"evaluate_ins",u"fit_ins",b"fit_ins",u"get_parameters",b"get_parameters",u"msg",b"msg",u"reconnect",b"reconnect"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"evaluate_ins",b"evaluate_ins",u"fit_ins",b"fit_ins",u"get_parameters",b"get_parameters",u"msg",b"msg",u"reconnect",b"reconnect"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"msg",b"msg"]) -> typing_extensions___Literal["reconnect","get_parameters","fit_ins","evaluate_ins"]: ...
type___ServerMessage = ServerMessage

class ClientMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Disconnect(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        reason: type___ReasonValue = ...

        def __init__(self,
            *,
            reason : typing___Optional[type___ReasonValue] = None,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"reason",b"reason"]) -> None: ...
    type___Disconnect = Disconnect

    class ParametersRes(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def parameters(self) -> type___Parameters: ...

        def __init__(self,
            *,
            parameters : typing___Optional[type___Parameters] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"parameters",b"parameters"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"parameters",b"parameters"]) -> None: ...
    type___ParametersRes = ParametersRes

    class FitRes(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        num_examples: builtin___int = ...
        num_examples_ceil: builtin___int = ...
        fit_duration: builtin___float = ...

        @property
        def parameters(self) -> type___Parameters: ...

        def __init__(self,
            *,
            parameters : typing___Optional[type___Parameters] = None,
            num_examples : typing___Optional[builtin___int] = None,
            num_examples_ceil : typing___Optional[builtin___int] = None,
            fit_duration : typing___Optional[builtin___float] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"parameters",b"parameters"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"fit_duration",b"fit_duration",u"num_examples",b"num_examples",u"num_examples_ceil",b"num_examples_ceil",u"parameters",b"parameters"]) -> None: ...
    type___FitRes = FitRes

    class EvaluateRes(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        num_examples: builtin___int = ...
        loss: builtin___float = ...
        accuracy: builtin___float = ...

        def __init__(self,
            *,
            num_examples : typing___Optional[builtin___int] = None,
            loss : typing___Optional[builtin___float] = None,
            accuracy : typing___Optional[builtin___float] = None,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"accuracy",b"accuracy",u"loss",b"loss",u"num_examples",b"num_examples"]) -> None: ...
    type___EvaluateRes = EvaluateRes


    @property
    def disconnect(self) -> type___ClientMessage.Disconnect: ...

    @property
    def parameters_res(self) -> type___ClientMessage.ParametersRes: ...

    @property
    def fit_res(self) -> type___ClientMessage.FitRes: ...

    @property
    def evaluate_res(self) -> type___ClientMessage.EvaluateRes: ...

    def __init__(self,
        *,
        disconnect : typing___Optional[type___ClientMessage.Disconnect] = None,
        parameters_res : typing___Optional[type___ClientMessage.ParametersRes] = None,
        fit_res : typing___Optional[type___ClientMessage.FitRes] = None,
        evaluate_res : typing___Optional[type___ClientMessage.EvaluateRes] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"disconnect",b"disconnect",u"evaluate_res",b"evaluate_res",u"fit_res",b"fit_res",u"msg",b"msg",u"parameters_res",b"parameters_res"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"disconnect",b"disconnect",u"evaluate_res",b"evaluate_res",u"fit_res",b"fit_res",u"msg",b"msg",u"parameters_res",b"parameters_res"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"msg",b"msg"]) -> typing_extensions___Literal["disconnect","parameters_res","fit_res","evaluate_res"]: ...
type___ClientMessage = ClientMessage
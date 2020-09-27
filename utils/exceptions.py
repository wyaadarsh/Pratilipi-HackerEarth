from logging import getLogger

logger = getLogger(__name__)


class BaseError(Exception):
    def __init__(self, args):
        logger.exception(args)
        super(BaseError, self).__init__(args)
        print(args)


class InvalidMoveException(BaseError):
    def __init__(self):
        errorString = "Invalid Move"
        errorCode = 430
        args = {"code": errorCode, "Description": errorString}
        super(InvalidMoveException, self).__init__(args)


class InvalidArgumentException(BaseError):

    def __init__(self, arg):
        errorString = "Invalid Argument: {}".format(arg)
        errorCode = 410
        arg = {"code": errorCode, "Description": errorString}
        super(InvalidArgumentException, self).__init__(arg)


class RequiredParamError(BaseError):

    def __init__(self, arg):
        super(RequiredParamError, self).__init__(arg)


class IDNeededException(BaseError):

    def __init__(self):
        errorString = "Unique id needed:"
        errorCode = 410
        arg = {"code": errorCode, "Description": errorString}
        super(IDNeededException, self).__init__()


class InvalidGameIDException(BaseError):

    def __init__(self):
        errorString = "Invalid id provided:"
        errorCode = 410
        arg = {"code": errorCode, "Description": errorString}
        super(InvalidGameIDException, self).__init__()

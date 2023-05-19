class ILensErrors(Exception):
    """Generic iLens Error"""


class KairosDBError(ILensErrors):
    """Kairos DB Error"""


class AuthenticationError(ILensErrors):
    pass


class DataFrameFormationError(ILensErrors):
    """Raise when there is an error during dataframe formation"""


class ErrorMessages:
    UNKNOWN_ERROR = "Error occurred while processing your request."
    ERROR001 = "Authentication Failed. Please verify token"
    ERROR002 = "Signature Expired"
    ERROR003 = "Signature Not Valid"
    ERROR004 = "No Data available to form dataframe"
    ERROR005 = "Error occurred While forming chart"
    ERROR006 = "Data Not Found"
    ERROR007 = "Error while reading initial parameters. Ensure Type is set with valid arguments."
    ERROR008 = "Failed to add Annotation"
    ERROR009 = "Unknown Error while fetching chart data"
    ERROR010 = "File not Found"
    ERROR011 = "Chart Not Implemented"
    ERROR012 = "SQL Query Formation Error"
    K_ERROR1 = "Data Not Found in Time series Database"
    K_ERROR2 = "Time series Database returned with an error"
    K_ERROR3 = "Communication Error with Time series Database"
    DF_ERROR1 = "Error occurred while forming Dataframe"
    DF_ERROR2 = "Given group-by parameters are invalid"
    META_ERROR1 = "Tags not Found in Meta"
    SPC_ERRO2 = "Not Enough Data"
    REQUEST_ERROR = "Request Error"
    SPC_ERR01 = "Data not found in SPC tag"
    CHART_ERROR = "Error occurred While forming chart"
    COMMON_MESSAGE = "Exception while updating: "
    CONNECTION_EXCEPTION = "Exception while closing connection: "
    DASHLIST_ERROR = "Error occurred in server while listing dashboards"


class IllegalTimeSelectionError(ILensErrors):
    pass


class TemplateFormationError(ILensErrors):
    pass


class ProductsNotFoundError(ILensErrors):
    """Raise when products matching conditions are not found"""

    pass


class DataNotFound(ILensErrors):
    """
    Raise when data is not found
    """


class TagDetailsNotFound(Exception):
    """
    Raise when tag details are crucial to proceed and meta service returns empty list
    """


class DuplicateName(ILensErrors):
    pass


class InputRequestError(Exception):
    pass


class JWTDecodingError(Exception):
    pass


class DashboardNotFound(ILensErrors):
    pass


class WidgetsNotFound(ILensErrors):
    pass


class JobCreationError(Exception):
    """
    Raised when a Job Creation throws an exception.

    Job Creation happens by adding a record to Mongo.
    """


class TemplateNotFoundError(Exception):
    """
    This error is raised when Dashboard/Widget Template is not found
    """


class ChartFormationError(Exception):
    pass


class QueryFormationError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


class PostgresDBError(Exception):
    pass


class CustomError(Exception):
    pass

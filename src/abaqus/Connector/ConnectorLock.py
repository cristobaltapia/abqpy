from abaqusConstants import *
from .ConnectorBehaviorOption import ConnectorBehaviorOption


class ConnectorLock(ConnectorBehaviorOption):
    """The ConnectorLock object defines locking criteria for one or more available components
    of a connector's relative motion.
    The ConnectorLock object is derived from the ConnectorBehaviorOption object.

    Attributes
    ----------
    lockingComponent
        The SymbolicConstant ALL or an Int specifying the motion components that are locked. If
        an Int is specified, only that motion component is locked when the locking criteria are
        satisfied. If **lockingComponent** = ALL, all motion components are locked. The default
        value is ALL.
    minMotion
        None or a Float specifying the lower bound for the connector's relative position for all
        specified components, or no lower bound. The default value is None.
    maxMotion
        None or a Float specifying the upper bound for the connector's relative position for all
        specified components, or no upper bound. The default value is None.
    minForce
        None or a Float specifying the lower bound of the force or moment in the directions of
        the specified components at which locking occurs, or no lower bound. The default value
        is None.
    maxForce
        None or a Float specifying the upper bound of the force or moment in the directions of
        the specified components at which locking occurs, or no upper bound. The default value
        is None.
    components
        A sequence of Ints specifying the components of relative motion for which the behavior
        is defined. Possible values are 1 ≤≤ **components** ≤≤ 6. Only available components can be
        specified. The default value is an empty sequence.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import section
        mdb.models[name].sections[name].behaviorOptions[i]
        import odbSection
        session.odbs[name].sections[name].behaviorOptions[i]

    The corresponding analysis keywords are:

    - CONNECTOR LOCK
    """

    # The SymbolicConstant ALL or an Int specifying the motion components that are locked. If
    # an Int is specified, only that motion component is locked when the locking criteria are
    # satisfied. If **lockingComponent** = ALL, all motion components are locked. The default
    # value is ALL.
    lockingComponent: SymbolicConstant = ALL

    # None or a Float specifying the lower bound for the connector's relative position for all
    # specified components, or no lower bound. The default value is None.
    minMotion: float = None

    # None or a Float specifying the upper bound for the connector's relative position for all
    # specified components, or no upper bound. The default value is None.
    maxMotion: float = None

    # None or a Float specifying the lower bound of the force or moment in the directions of
    # the specified components at which locking occurs, or no lower bound. The default value
    # is None.
    minForce: float = None

    # None or a Float specifying the upper bound of the force or moment in the directions of
    # the specified components at which locking occurs, or no upper bound. The default value
    # is None.
    maxForce: float = None

    # A sequence of Ints specifying the components of relative motion for which the behavior
    # is defined. Possible values are 1 ≤≤ **components** ≤≤ 6. Only available components can be
    # specified. The default value is an empty sequence.
    components: tuple = ()

    def __init__(
        self,
        lockingComponent: SymbolicConstant = ALL,
        minMotion: float = None,
        maxMotion: float = None,
        minForce: float = None,
        maxForce: float = None,
        components: tuple = (),
    ):
        """This method creates a connector lock behavior option for a ConnectorSection.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

                      import connectorBehavior
                      connectorBehavior.ConnectorLock
                      import odbConnectorBehavior
                      odbConnectorBehavior.ConnectorLock

        Parameters
        ----------
        lockingComponent
            The SymbolicConstant ALL or an Int specifying the motion components that are locked. If
            an Int is specified, only that motion component is locked when the locking criteria are
            satisfied. If **lockingComponent** = ALL, all motion components are locked. The default
            value is ALL.
        minMotion
            None or a Float specifying the lower bound for the connector's relative position for all
            specified components, or no lower bound. The default value is None.
        maxMotion
            None or a Float specifying the upper bound for the connector's relative position for all
            specified components, or no upper bound. The default value is None.
        minForce
            None or a Float specifying the lower bound of the force or moment in the directions of
            the specified components at which locking occurs, or no lower bound. The default value
            is None.
        maxForce
            None or a Float specifying the upper bound of the force or moment in the directions of
            the specified components at which locking occurs, or no upper bound. The default value
            is None.
        components
            A sequence of Ints specifying the components of relative motion for which the behavior
            is defined. Possible values are 1 ≤≤ **components** ≤≤ 6. Only available components can be
            specified. The default value is an empty sequence.

        Returns
        -------
        ConnectorLock
            A :py:class:`~abaqus.Connector.ConnectorLock.ConnectorLock` object.

        Raises
        ------
        ValueError and TextError
        """
        super().__init__()
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the ConnectorLock object.

        Raises
        ------
        ValueError
        """
        pass

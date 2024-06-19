from __future__ import annotations
from typing import TypeAlias

import auto_all

from abqpy import run  # noqa

run(cae=True)
auto_all.start_all()

from math import *  # noqa

from .builtin import *  # noqa
from .Canvas.Highlight import *  # noqa
from .Mdb.Mdb import Mdb  # noqa
from .Mdb.MdbCommands import *  # noqa
from .Odb.Odb import Odb  # noqa
from .Session.Session import Session  # noqa
from .UtilityAndView import abaqusConstants  # noqa
from .UtilityAndView.abaqusConstants import OFF, Boolean  # noqa
from .UtilityAndView.BackwardCompatibility import BackwardCompatibility  # noqa
from .UtilityAndView.SymbolicConstant import SymbolicConstant  # noqa
from .UtilityAndView.User import *  # noqa

session = Session()
mdb = Mdb()

from abaqus.Model.Model import Model# as ModelType

ModelType = NewType("Model", Model)

backwardCompatibility = BackwardCompatibility()

YES = abaqusConstants.YES
NO = abaqusConstants.NO

auto_all.end_all()

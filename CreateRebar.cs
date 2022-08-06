using System;
using System.Collections.Generic;
using Autodesk.DesignScript.Geometry;
using Autodesk.Revit.DB;
using Autodesk.Revit.DB.Structure;
using DynamoServices;
using Revit.Elements.Views;
using Revit.GeometryConversion;
using RevitServices.Persistence;
using RevitServices.Transactions;
using Arc = Autodesk.Revit.DB.Arc;
using Curve = Autodesk.Revit.DB.Curve;
using Line = Autodesk.Revit.DB.Line;
using Autodesk.DesignScript.Runtime;


namespace BIM3DM
{
    [IsVisibleInDynamoLibrary(true)]
    public class CreateRebar
    {
        public Element CreateRebarBIM3DTest1(RebarStyle rebarStyle, RebarBarType rebarBarType, RebarHookType startHook, RebarHookType endHook, string idFromString, XYZ normal, IList<Curve> curve, RebarHookOrientation startHookOrientation, RebarHookOrientation endHookOrientation, bool useExistingShape, bool createNewShape)
        {
            Document currentDBDocument = DocumentManager.Instance.CurrentDBDocument;
            TransactionManager.Instance.EnsureInTransaction(currentDBDocument);
            List<Curve> list = new List<Curve>();
            int idInt = Convert.ToInt32(idFromString);
            ElementId id = new ElementId(idInt);
            Element eFromId = currentDBDocument.GetElement(id);
            Rebar rebar = Rebar.CreateFromCurves(currentDBDocument, rebarStyle, rebarBarType, startHook, endHook, eFromId, normal, curve, startHookOrientation, endHookOrientation, useExistingShape, createNewShape);
            TransactionManager.Instance.TransactionTaskDone();
            return rebar;
        }
        public Element CreateRebarBIM3DTest2(Autodesk.Revit.DB.Document document, FamilyInstance column, RebarBarType barType, RebarHookType hookType)

        {
            // Define the rebar geometry information - Line rebar
            LocationPoint location = column.Location as LocationPoint;
            XYZ origin = location.Point;
            XYZ normal = new XYZ(1, 0, 0);
            // create rebar 9' long
            XYZ rebarLineEnd = new XYZ(origin.X, origin.Y, origin.Z + 9);
            Line rebarLine = Line.CreateBound(origin, rebarLineEnd);

            // Create the line rebar
            IList<Curve> curves = new List<Curve>();
            curves.Add(rebarLine);

            Rebar rebar = Rebar.CreateFromCurves(document, Autodesk.Revit.DB.Structure.RebarStyle.Standard, barType, hookType, hookType,
                                column, origin, curves, RebarHookOrientation.Right, RebarHookOrientation.Left, true, true);

            return rebar;
        }
    }
}



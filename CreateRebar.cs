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
        //public Element CreateRebarBIM3DM(IList<Curve> curve, RebarBarType barType, RebarStyle barStyle, FamilyInstance column, RebarHookType hookType, RebarHookType endHook, XYZ normal, bool useExistingShape, bool createNewShape)
        public Element CreateRebarBIM3DM( FamilyInstance column, RebarBarType barType, RebarHookType hookType)
        {
            Document currentDBDocument = DocumentManager.Instance.CurrentDBDocument;

            // Define the rebar geometry information - Line rebar
            LocationPoint location = column.Location as LocationPoint;
            XYZ origin = location.Point;
            XYZ normal = new XYZ(1, 0, 0);
            // create rebar 9' long
            XYZ rebarLineEnd = new XYZ(origin.X, origin.Y, origin.Z + 9);
            Line rebarLine = Line.CreateBound(origin, rebarLineEnd);
            TransactionManager.Instance.EnsureInTransaction(currentDBDocument);

            // Create the line rebar
            IList<Curve> curves = new List<Curve>();
            curves.Add(rebarLine);
            Rebar rebar = Rebar.CreateFromCurves(currentDBDocument, Autodesk.Revit.DB.Structure.RebarStyle.Standard, barType, hookType, hookType,
                                column, origin, curves, RebarHookOrientation.Right, RebarHookOrientation.Left, true, true);
            return rebar;
        }
    }
}

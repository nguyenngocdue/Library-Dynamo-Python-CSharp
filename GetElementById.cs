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
    public class GetElementById
    {
        public Element getElementByID( string idFromString)
        {
            Document currentDBDocument = DocumentManager.Instance.CurrentDBDocument;
            int idInt = Convert.ToInt32(idFromString);
            ElementId id = new ElementId(idInt);
            Element eFromId = currentDBDocument.GetElement(id);
            return eFromId;
        }
    }
}

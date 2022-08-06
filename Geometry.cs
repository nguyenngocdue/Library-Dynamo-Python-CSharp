using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Autodesk.DesignScript.Runtime;
using RevitServices.Persistence;
using Revit.GeometryConversion;
using Revit.Elements;
using RevitServices.Transactions;
using Autodesk.Revit.DB;

namespace BIM3DM
{
    public class Geometry     
    {
        [IsVisibleInDynamoLibrary(true)]
        public static BoundingBoxXYZ Crop_box(BoundingBoxXYZ bbox, int offset)
        {
            var minx = bbox.Min.X - offset;
            var miny = bbox.Min.Y - offset;
            var minz = bbox.Min.Z - offset;
            var maxx = bbox.Max.X + offset;
            var maxy = bbox.Max.Y + offset;
            var maxz = bbox.Max.Z + offset;

            var newbox = new BoundingBoxXYZ
            {
                Min = new XYZ(minx, miny, minz),
                Max = new XYZ(maxx, maxy, maxz)
            };

            return newbox;
        }
    }

    public static class ElementGraphics
    {
        [IsVisibleInDynamoLibrary(true)]
        public static List <Revit.Elements.Element> CopyPateFilter (Revit.Elements.Views.View ViewToCopy, List<Revit.Elements.Views.View> ViewToPaste)
        {
            var filtersId = new List<ElementId>();
            var settings = new List<OverrideGraphicSettings>();
            var visibility = new List<Boolean>();
            var Views = new List<Revit.Elements.Element>();
            var viewtocopy = (Autodesk.Revit.DB.View)ViewToCopy.InternalElement;
            foreach (var id in viewtocopy.GetFilters())
            {
                filtersId.Add(id);
                settings.Add(viewtocopy.GetFilterOverrides(id));
                visibility.Add(viewtocopy.GetFilterVisibility(id));
            }
            TransactionManager.Instance.EnsureInTransaction(DocumentManager.Instance.CurrentDBDocument);
            foreach (var pview in ViewToPaste)
            {
                var pasteview = (Autodesk.Revit.DB.View)pview.InternalElement;
                foreach(var i in filtersId.Zip(settings, Tuple.Create))
                {
                    pasteview.SetFilterOverrides(i.Item1, i.Item2);
                }
                foreach (var j in filtersId.Zip(visibility, Tuple.Create))
                {
                    pasteview.SetFilterVisibility(j.Item1, j.Item2);
                }
                Views.Add(pview);
            }
            TransactionManager.Instance.TransactionTaskDone();
            return Views;
        }

        [IsVisibleInDynamoLibrary(true)]
        public static String HideUnHideElement( List<Revit.Elements.Element> Elements, List<Revit.Elements.Element> Views, Boolean HideUnhide = false)
        {
            var ids = new List<ElementId>();
            TransactionManager.Instance.EnsureInTransaction(DocumentManager.Instance.CurrentDBDocument);
            foreach (var elem in Elements)
            {
                var id = (Autodesk.Revit.DB.Element)elem.InternalElement;
                ids.Add(id.Id);
            }
            foreach (var view in Views)
            {
                if (HideUnhide == true)
                {
                    var v = (Autodesk.Revit.DB.View)view.InternalElement;
                    v.HideElements(ids);
                    
                }
                else
                {
                    var v = (Autodesk.Revit.DB.View)view.InternalElement;
                    v.UnhideElements(ids);
                }
                TransactionManager.Instance.TransactionTaskDone();
            }
            return "Done!";
        }
    }
}

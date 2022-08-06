using System;
using System.Collections.Generic;
using System.Runtime.CompilerServices;
using Autodesk.DesignScript.Geometry;
using Autodesk.Revit.DB;
using Autodesk.Revit.DB.Structure;
using DynamoServices;
using Revit.Elements.Views;
using Revit.GeometryConversion;
using RevitServices.Persistence;

namespace BIM3DM
{
 //   public partial class Rebar
 //   {
 //       public static Rebar ByCurve(List<Autodesk.DesignScript.Geometry.Curve> curve, int hostElementId, string rebarStyle, ElementType rebarBarType, 
 //           string startHookOrientation, string endHookOrientation, ElementType startHookType, ElementType endHookType, Vector vector)
	//	{
	//		if (curve == null)
	//		{
	//			throw new ArgumentNullException("Input Curve missing");
	//		}
	//		if (rebarStyle == null)
	//		{
	//			throw new ArgumentNullException("Rebar Style missing");
	//		}
	//		if (rebarBarType == null)
	//		{
	//			throw new ArgumentNullException("Rebar Bar Type missing");
	//		}
	//		if (startHookOrientation == null)
	//		{
	//			throw new ArgumentNullException("Start Hook Orientation missing");
	//		}
	//		if (endHookOrientation == null)
	//		{
	//			throw new ArgumentNullException("End Hook Orientation missing");
	//		}
	//		if (vector == null)
	//		{
	//			throw new ArgumentNullException("Normal Vector missing");
	//		}
	//		ElementId elementId = new ElementId(hostElementId);
	//		if (elementId == ElementId.InvalidElementId)
	//		{
	//			throw new ArgumentNullException("Host ElementId error");
	//		}
	//		Element element = DocumentManager.Instance.CurrentDBDocument.GetElement(elementId);
	//		RebarStyle barStyle = RebarStyle.Standard;
	//		Enum.TryParse<RebarStyle>(rebarStyle, out barStyle);
	//		RebarHookOrientation startHookOrientation2 = RebarHookOrientation.Left;
	//		Enum.TryParse<RebarHookOrientation>(startHookOrientation, out startHookOrientation2);
	//		RebarHookOrientation endHookOrientation2 = RebarHookOrientation.Left;
	//		Enum.TryParse<RebarHookOrientation>(endHookOrientation, out endHookOrientation2);
	//		RebarHookType startHook = (startHookType == null) ? null : ((RebarHookType)startHookType);
	//		RebarHookType endHook = (endHookType == null) ? null : ((RebarHookType)endHookType);

	//		return new Rebar(curve.ApproximateToRvt(), (RebarBarType)rebarBarType, barStyle, element, startHook, endHook, startHookOrientation2, endHookOrientation2, GeometryPrimitiveConverter.ToRevitType(vector, false), true, true);
	//	}
	//}
}

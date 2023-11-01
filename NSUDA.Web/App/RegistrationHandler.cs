namespace NSUDA.Handler
{
    using System.Reflection;

    /// <summary>
    /// Provides functional for register <see cref="RequestDelegate"/> methods.
    /// </summary>
    internal static partial class RegistrationHandler
    {
        /// <summary>
        /// Register the all methods with HandlerPath attribute.
        /// Start the all register methods from this class.
        /// </summary>
        internal static void RegistrateAll(WebApplication application)
        {
            MethodInfo[] handlers = typeof(Handler).GetMethods(
                BindingFlags.NonPublic
                | BindingFlags.Static
            );

            foreach (var handler in handlers)
            {
                Attribute? attribute = 
                    Attribute.GetCustomAttribute(handler, 
                        typeof(HandlerPathAttribute));
                if (attribute is HandlerPathAttribute attr)
                {
                    application.Map(attr.Path, async(context) => 
                    {
                        object[] param = new object[] { context };
                        await (Task)handler?.Invoke(null, param)!;
                    });
                }
            }
        }
    }



}
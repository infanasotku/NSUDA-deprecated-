namespace NSUDA.Handler
{
    using System.Reflection;

    /// <summary>
    /// Provides functional for register <see cref="RequestDelegate"/> methods.
    /// </summary>
    internal static class RegistrationHandler
    {
        /// <summary>
        /// Register the all methods with HandlerPath attribute.
        /// </summary>
        internal static void RegistrateAll(WebApplication application)
        {
            MethodInfo[] handlers = typeof(Handler).GetMethods(
                BindingFlags.Instance | BindingFlags.NonPublic
                | BindingFlags.Static
            );

            foreach (var handler in handlers)
            {
                Attribute? attribute = 
                    Attribute.GetCustomAttribute(handler, typeof(HandlerPathAttribute));
                if (attribute is HandlerPathAttribute attr)
                {
                    application.Map(attr.path, async(context) => 
                    {
                        object[] param = new object[] { context };
                        await (Task)handler?.Invoke(null, param)!;
                    });
                }
            }
        }
    }



}
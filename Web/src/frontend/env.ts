export const globalEnv = {
    apiUri: 'http://localhost:5000/api',
    redirectUri: 'http://localhost:5001/auth/',
}

export const googleEnv = {
    clientID: '381287486388-a5hpo58arf5l1d2ic46cahvvnc1kupnq.apps.googleusercontent.com',
    scope: 'email openid profile',
    accessType: 'offline',
    openIDConfigUri: 'https://accounts.google.com/.well-known/openid-configuration'
}

export const vkEnv = {
    authUri: 'https://oauth.vk.com/authorize',
    clientID: '51871808',
    scope: 'email photos'
}
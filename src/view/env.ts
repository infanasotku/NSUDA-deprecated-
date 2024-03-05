export const globalEnv = {
    apiUri: 'http://localhost:5000/api'
}

export const googleEnv = {
    googleClientID: '381287486388-a5hpo58arf5l1d2ic46cahvvnc1kupnq.apps.googleusercontent.com',
    scope: 'email openid profile',
    redirectUri: 'http://localhost:5001/auth/',
    accessType: 'offline',
    openIDConfigUri: 'https://accounts.google.com/.well-known/openid-configuration'
}
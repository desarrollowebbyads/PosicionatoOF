const { remote } = require('webdriverio');
require('dotenv').config();

(async () => {
    const browser = await remote({
        capabilities: {
            browserName: 'firefox'
        }
    });

    await browser.url('https://onlyfans.com/my/statements/earnings');

    try {
        // Buscar elementos por querySelectorAll
        const emailInput = await browser.$('v-input__slot');
        const passwordInput = await browser.$('.v-input__slot');
        const loginButton = await browser.$('.g-btn');

        // Obtener las credenciales del entorno
        const username = process.env.USERNAME;
        const password = process.env.PASSWORD;

        if (!username || !password) {
            console.error("Error: Las variables de entorno para el nombre de usuario y la contraseña no están establecidas.");
            return;
        }

        // Ingresar las credenciales y hacer clic en el botón de inicio de sesión
        await emailInput.setValue(username);
        await passwordInput.setValue(password);
        await loginButton.click();

        // Esperar a que aparezcan los datos de ingresos
        const datosIngresosElement = await browser.$('.b-stats-row__val');
        const datosIngresos = await datosIngresosElement.getText();
        console.log("Ingresos diarios:", datosIngresos);

    } catch (error) {
        console.error("Error:", error.message);
    } finally {
        await browser.deleteSession();
    }
})();
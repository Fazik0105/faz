import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import './index.css';




import { ChakraProvider } from '@chakra-ui/react';
import { ColorModeScript } from '@chakra-ui/react';
import { BrowserRouter as Router } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";




import {theme} from "./theme";


ReactDOM.render(
    
    <ChakraProvider>
        <ColorModeScript initialColorMode={theme.config.initialColorMode} />
        <React.StrictMode>
            <Router>
                <App />
            </Router>
        </React.StrictMode>
    </ChakraProvider>, 
    
    document.getElementById("root")
    );
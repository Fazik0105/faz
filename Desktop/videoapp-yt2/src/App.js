import React, { useEffect, useState } from "react";
import { Container, Row, Col } from "react-bootstrap";
import { Route, Routes, useNavigate } from "react-router-dom";
import Admin from "./Container/Admin";
import Home from "./Container/Home";
import Login from "./Container/Login";
import Create from "./Container/Create";
import { fetchUser, userAccessToken } from "./utils/fetchUser";
import ProtectedRoute from "./ComponentsLogin/ProtectedRoute";
import { UserAuthContextProvider } from "./context/UserAuthContext";

const App = () => {
  const [user, setUser] = useState(null);
  const navigate = useNavigate();


  useEffect(() => {
    const accessToken = userAccessToken();
    if (!accessToken) {
      navigate("/login", { replace: true });
    } else {
      const [userInfo] = fetchUser();
      setUser(userInfo);
    }
  }, []);

  return (
    <UserAuthContextProvider>
      <Routes>
        <Route
          path="/*"
          element={
            <ProtectedRoute>
              <Home user={user}/>
            </ProtectedRoute>
          }
        />
        <Route path="/login" element={<Login />} />
        <Route path="/admin" element={<Admin />} />
        <Route path="/create" element={<Create />} />
        <Route path="/home" element={<Home user={user}/>} />
      </Routes>
    </UserAuthContextProvider>
  );
};

export default App;

import React, { useState } from "react";
import { Flex } from "@chakra-ui/react";
import {
  Category,
  Create,
  Feed,
  NavBarAdmin,
  Search,
  UserProfile,
  VideoPinDetail,
} from "../Components";
import { Routes, Route } from "react-router-dom";
import { categories } from "../data";

const Admin = ({ user }) => {
  const [searchTerm, setsearchTerm] = useState("");
  return (
    <>
      <NavBarAdmin user={user} setsearchTerm={setsearchTerm} />

      <Flex width={"100vw"}>
        <Flex
          direction={"column"}
          justifyContent="start"
          alignItems={"center"}
          width="5%"
        >
          {categories &&
            categories.map((data) => <Category key={data.id} data={data} />)}
        </Flex>

        <Flex
          width={"95%"}
          px={4}
          justifyContent="center"
          alignItems={"center"}
        >
          <Routes>
            <Route path="/" element={<Feed />} />
            <Route path="/category/:categoryId" element={<Feed />} />
            <Route path="/create" element={<Create />} />
            <Route path="/videoDetail/:videoId" element={<VideoPinDetail />} />
            <Route
              path="/search"
              element={<Search searchTerm={searchTerm} />}
            />
            <Route path="/userDetail/:userId" element={<UserProfile />} />
          </Routes>
        </Flex>
      </Flex>
    </>
  );
};

export default Admin;
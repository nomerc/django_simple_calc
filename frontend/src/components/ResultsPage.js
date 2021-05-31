import React from "react";
import { Grid } from "@material-ui/core";
import { useFetch } from "../hooks/useFetch";
import SortableOperationsTable from "./SortableOperationsTable";

export const ResultsPage = ({ args: { arg1, arg2 }, op }) => {
  const requestOptions = {
    method: "POST",
    headers: { "Content-type": "application/json" },
    body: JSON.stringify({ arg1, arg2, operation_name: op }),
  };

  const res = useFetch("api/calc", requestOptions);

  if (!res.response) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <Grid container direction="row" justify="center" alignItems="center">
        <h1>
          Latest operation:
          {" " +
            res.response["arg1"] +
            " " +
            res.response["operation_name"] +
            " " +
            res.response["arg2"] +
            " = " +
            res.response["result"]}
        </h1>
      </Grid>
      <SortableOperationsTable />
      {/* <OperationsTable /> */}
    </div>
  );
};

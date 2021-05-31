import React, { useState } from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import { Grid, Button, ButtonGroup, TextField } from "@material-ui/core";
import { ResultsPage } from "./ResultsPage";

export const HomePage = () => {
  const [_args, setArgs] = useState({ arg1: 1, arg2: 1 });
  const [_op, setOp] = useState(null);

  return (
    <div>
      <Grid container direction="row" justify="center" alignItems="center">
        <Router>
          <Switch>
            <Route exact path="/">
              <TextField
                id="arg1"
                label="Input first arg"
                onChange={(e) => {
                  setArgs({ ..._args, arg1: e.target.value });
                }}
              />
              <TextField
                id="arg2"
                label="Input second arg"
                onChange={(e) => {
                  setArgs({ ..._args, arg2: e.target.value });
                }}
              />
              <ButtonGroup
                variant="contained"
                color="primary"
                aria-label="contained primary button group"
                to="/results"
                component={Link}
              >
                <Button
                  onClick={() => {
                    setOp("+");
                  }}
                >
                  +
                </Button>
                <Button
                  onClick={() => {
                    setOp("-");
                  }}
                >
                  -
                </Button>
                <Button
                  onClick={() => {
                    setOp("*");
                  }}
                >
                  *
                </Button>
              </ButtonGroup>
            </Route>
            <Route path="/results">
              <ResultsPage args={_args} op={_op} />
            </Route>
          </Switch>
        </Router>
      </Grid>
    </div>
  );
};

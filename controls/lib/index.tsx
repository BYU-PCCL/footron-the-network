/** @jsxImportSource @emotion/react */
import { css } from "@emotion/react";
import React, { useState } from "react";
import { useMessaging } from "@footron/controls-client";
import {
  FormControl,
  NativeSelect,
  InputLabel,
  Checkbox,
  FormControlLabel,
  FormGroup, Slider
} from "@material-ui/core";
import { useCallback } from "react";

const containerStyle = css`
  padding: 16px;
  overflow-x: hidden;

  p {
    margin: 0 0 16px;
  }
`;

const buildings = [
  "ASB",
  "B66",
  "BNSN",
  "BRMB",
  "BRWB",
  "BYUB",
  "CANC",
  "CB",
  "CONF",
  "CTB",
  "EB",
  "ERL",
  "ESC",
  "HBLL",
  "HC",
  "HCEB",
  "HFAC",
  "HGB",
  "HRCB",
  "HRCN",
  "IPF",
  "ITB",
  "JFSB",
  "JKB",
  "JRCB",
  "JSB",
  "KMBL",
  "LSB",
  "LVES",
  "MARB",
  "MB",
  "MC",
  "MCA",
  "MCKB",
  "MLBM",
  "MOA",
  "MSRB",
  "RB",
  "SAB",
  "SFH",
  "SHC",
  "SNLB",
  "TLRB",
  "TMCB",
  "TNRB",
  "ULB",
  "UPC",
  "WSC"
]

const marks = [
  {
    value: 0,
    label: "12"
  },
  {
    value: 12,
    label: "12"
  },
  {
    value: 24,
    label: "12"
  },
];

marks.push(...[...Array(5).keys()].map((i: number) => {
  return {
    value: (i * 2) + 2,
    label: `${(i * 2) + 2}`,
  }
}));

marks.push(...[...Array(5).keys()].map((i: number) => {
  return {
    value: (i * 2) + 14,
    label: `${(i * 2) + 2}`,
  }
}));

const ControlsComponent = (): JSX.Element => {
  const [building, setBuilding] = useState<string>("");
  const [preciseRooms, setPreciseRooms] = useState<boolean>(false);

  const [step, setStep] = useState<number | undefined>(undefined);
  const [actualStep, setActualStep] = useState<number>(0);

  const { sendMessage } = useMessaging<any>((message) => {
    if (message.type === "step") {
      setActualStep((message.step / 3600));
    }
  });

  const updateSlider = useCallback(
    async (event, value) => {
      console.log(value)
      setStep(value);
      console.log(value * 3600);
      await sendMessage({ type: "step", step: Math.floor(value * 3600) });
    },
    [sendMessage]
  );

  const updateSliderCommitted = useCallback(
    async (event, value) => {
      await sendMessage({ type: "step", step: Math.floor(value * 3600) });
      setStep(undefined);
      setActualStep(value);
    },
    [sendMessage]
  );

  const handleBuildingChange = (event: React.ChangeEvent<{ name?: string; value: string }>) => {
    const building = event.target.value;
    setBuilding(building);
    sendMessage({ "type": "building", "building": building })
    // TODO: Send building message update here
  };

  const handleRoomPrecisionChange = (event: React.ChangeEvent<{ name?: string; checked: boolean }>) => {
    const preciseRooms = event.target.checked;
    setPreciseRooms(preciseRooms);
    sendMessage({ "type": "room_precision", "precise": preciseRooms })
    // TODO: Send building message update here
  };

  return (
    <div css={containerStyle}>
      <FormGroup>
        <p>
          <b>Change the time of day:</b>
        </p>
        <Slider
          min={0}
          max={24}
          onChange={updateSlider}
          onChangeCommitted={updateSliderCommitted}
          step={0.001}
          // step={0.00000001}
          marks={marks}
          value={(step ?? actualStep)}
        />
        <br/>
        <p>
          <b>Watch traffic to and from a specific building:</b>
        </p>
        <FormControl>
          <InputLabel htmlFor="building-native-helper">Building</InputLabel>
          <NativeSelect
            inputProps={{
              name: 'Building',
              id: 'building-native-helper',
            }}
            id="demo-simple-select"
            value={building}
            name="Building"
            onChange={handleBuildingChange}
          >
            <option value="all">All buildings</option>
            {
              buildings.map((building) => <option key={building} value={building}>{building}</option>)
            }
          </NativeSelect>
        </FormControl>
        <br/>
        <FormControlLabel control={<Checkbox checked={preciseRooms} onChange={handleRoomPrecisionChange}/>}
                          label="Precise room locations"/>
      </FormGroup>
    </div>
  );
};

export default ControlsComponent;

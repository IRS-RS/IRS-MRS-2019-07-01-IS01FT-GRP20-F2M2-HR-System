/*
 * Copyright 2015 Red Hat, Inc. and/or its affiliates.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package sg.edu.nus.iss.is2019.rs.hr.swingui;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Desktop;
import java.awt.event.ActionEvent;
import java.net.URL;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.swing.AbstractAction;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTabbedPane;
import javax.swing.SwingConstants;

import org.apache.commons.lang3.tuple.Pair;
import org.optaplanner.examples.common.swingui.SolutionPanel;
import org.optaplanner.examples.common.swingui.timetable.TimeTablePanel;
import org.optaplanner.swing.impl.SwingUtils;
import org.optaplanner.swing.impl.TangoColorFactory;

import sg.edu.nus.iss.is2019.rs.hr.domain.Day;
import sg.edu.nus.iss.is2019.rs.hr.domain.MeetingAssignment;
import sg.edu.nus.iss.is2019.rs.hr.domain.MeetingSchedule;
import sg.edu.nus.iss.is2019.rs.hr.domain.Person;
import sg.edu.nus.iss.is2019.rs.hr.domain.PreferredAttendance;
import sg.edu.nus.iss.is2019.rs.hr.domain.RequiredAttendance;
import sg.edu.nus.iss.is2019.rs.hr.domain.Room;
import sg.edu.nus.iss.is2019.rs.hr.domain.TimeGrain;

import static org.apache.commons.lang3.ObjectUtils.*;
import static org.optaplanner.examples.common.swingui.timetable.TimeTablePanel.HeaderColumnKey.*;
import static org.optaplanner.examples.common.swingui.timetable.TimeTablePanel.HeaderRowKey.*;

public class MeetingSchedulingPanel extends SolutionPanel<MeetingSchedule> {

    public static final String LOGO_PATH = "/org/optaplanner/examples/meetingscheduling/swingui/meetingSchedulingLogo.png";

    private final TimeTablePanel<TimeGrain, Room> roomsPanel;
//    private final TimeTablePanel<TimeGrain, Pair<Person, Boolean>> personsPanel;
    private final OvertimeTimeGrain OVERTIME_TIME_GRAIN = new OvertimeTimeGrain();

    public MeetingSchedulingPanel() {
        setLayout(new BorderLayout());
        JTabbedPane tabbedPane = new JTabbedPane();
        roomsPanel = new TimeTablePanel<>();
        tabbedPane.add("Combinations", new JScrollPane(roomsPanel));
//        personsPanel = new TimeTablePanel<>();
//        tabbedPane.add("Persons", new JScrollPane(personsPanel));
        add(tabbedPane, BorderLayout.CENTER);
        setPreferredSize(PREFERRED_SCROLLABLE_VIEWPORT_SIZE);
    }

    @Override
    public boolean isWrapInScrollPane() {
        return false;
    }

    @Override
    public void resetPanel(MeetingSchedule meetingSchedule) {
        roomsPanel.reset();
//        personsPanel.reset();
        defineGrid(meetingSchedule);
        fillCells(meetingSchedule);
        repaint(); // Hack to force a repaint of TimeTableLayout during "refresh screen while solving"
    }

    private void defineGrid(MeetingSchedule meetingSchedule) {
        roomsPanel.defineColumnHeaderByKey(HEADER_COLUMN); // Room header
//        personsPanel.defineColumnHeaderByKey(HEADER_COLUMN_GROUP1); // Person header
//        personsPanel.defineColumnHeaderByKey(HEADER_COLUMN); // Required header
        for (TimeGrain timeGrain : meetingSchedule.getTimeGrainList()) {
            roomsPanel.defineColumnHeader(timeGrain);
//            personsPanel.defineColumnHeader(timeGrain);
        }
//        roomsPanel.defineColumnHeader(OVERTIME_TIME_GRAIN); // Overtime timeGrain
//        personsPanel.defineColumnHeader(OVERTIME_TIME_GRAIN); // Overtime timeGrain
        roomsPanel.defineColumnHeader(null); // Unassigned timeGrain
//        personsPanel.defineColumnHeader(null); // Unassigned timeGrain

        roomsPanel.defineRowHeaderByKey(HEADER_ROW_GROUP1); // Date header
        roomsPanel.defineRowHeaderByKey(HEADER_ROW); // TimeGrain header
        for (Room room : meetingSchedule.getRoomList()) {
            roomsPanel.defineRowHeader(room);
        }
        roomsPanel.defineRowHeader(null); // Unassigned

//        personsPanel.defineRowHeaderByKey(HEADER_ROW_GROUP1); // Day header
//        personsPanel.defineRowHeaderByKey(HEADER_ROW); // TimeGrain header
//        for (Person person : meetingSchedule.getPersonList()) {
//            personsPanel.defineRowHeader(Pair.of(person, Boolean.TRUE));
//            personsPanel.defineRowHeader(Pair.of(person, Boolean.FALSE));
//        }
    }

    private void fillCells(MeetingSchedule meetingSchedule) {
        roomsPanel.addCornerHeader(HEADER_COLUMN, HEADER_ROW, createTableHeader(new JLabel("Groups")));
        fillRoomCells(meetingSchedule);
//        personsPanel.addCornerHeader(HEADER_COLUMN_GROUP1, HEADER_ROW, createTableHeader(new JLabel("Person")));
//        personsPanel.addCornerHeader(HEADER_COLUMN, HEADER_ROW, createTableHeader(new JLabel("Attendance")));
//        fillPersonCells(meetingSchedule);
        fillTimeGrainCells(meetingSchedule);
        fillMeetingAssignmentCells(meetingSchedule);
    }

    private void fillRoomCells(MeetingSchedule meetingSchedule) {
        for (Room room : meetingSchedule.getRoomList()) {
            roomsPanel.addRowHeader(HEADER_COLUMN, room,
                    createTableHeader(new JLabel(room.getLabel(), SwingConstants.CENTER)));
        }
        roomsPanel.addRowHeader(HEADER_COLUMN, null,
                createTableHeader(new JLabel("Unassigned", SwingConstants.CENTER)));
    }

//    private void fillPersonCells(MeetingSchedule meetingSchedule) {
//        for (Person person : meetingSchedule.getPersonList()) {
//            personsPanel.addRowHeader(HEADER_COLUMN_GROUP1, Pair.of(person, Boolean.TRUE),
//                    HEADER_COLUMN_GROUP1, Pair.of(person, Boolean.FALSE),
//                    createTableHeader(new JLabel(person.getLabel(), SwingConstants.CENTER)));
//            personsPanel.addRowHeader(HEADER_COLUMN, Pair.of(person, Boolean.TRUE),
//                    createTableHeader(new JLabel("Required", SwingConstants.CENTER)));
//            personsPanel.addRowHeader(HEADER_COLUMN, Pair.of(person, Boolean.FALSE),
//                    createTableHeader(new JLabel("Preferred", SwingConstants.CENTER)));
//        }
//    }

    private void fillTimeGrainCells(MeetingSchedule meetingSchedule) {
        Map<Day, TimeGrain> firstTimeGrainMap = new HashMap<>(meetingSchedule.getDayList().size());
        Map<Day, TimeGrain> lastTimeGrainMap = new HashMap<>(meetingSchedule.getDayList().size());
        for (TimeGrain timeGrain : meetingSchedule.getTimeGrainList()) {
            Day day = timeGrain.getDay();
            TimeGrain firstTimeGrain = firstTimeGrainMap.get(day);
            if (firstTimeGrain == null || firstTimeGrain.getGrainIndex() > timeGrain.getGrainIndex()) {
                firstTimeGrainMap.put(day, timeGrain);
            }
            TimeGrain lastTimeGrain = lastTimeGrainMap.get(day);
            if (lastTimeGrain == null || lastTimeGrain.getGrainIndex() < timeGrain.getGrainIndex()) {
                lastTimeGrainMap.put(day, timeGrain);
            }
            roomsPanel.addColumnHeader(timeGrain, HEADER_ROW,
                    createTableHeader(new JLabel(timeGrain.getLabel())));
//            personsPanel.addColumnHeader(timeGrain, HEADER_ROW,
//                    createTableHeader(new JLabel(timeGrain.getLabel())));
        }
//        roomsPanel.addColumnHeader(OVERTIME_TIME_GRAIN, HEADER_ROW,
//                createTableHeader(new JLabel("Overtime")));
//        personsPanel.addColumnHeader(OVERTIME_TIME_GRAIN, HEADER_ROW,
//                createTableHeader(new JLabel("Overtime")));
        roomsPanel.addColumnHeader(null, HEADER_ROW,
                createTableHeader(new JLabel("Unassigned")));
//        personsPanel.addColumnHeader(null, HEADER_ROW,
//                createTableHeader(new JLabel("Unassigned")));

        for (Day day : meetingSchedule.getDayList()) {
            TimeGrain firstTimeGrain = firstTimeGrainMap.get(day);
            TimeGrain lastTimeGrain = lastTimeGrainMap.get(day);
            roomsPanel.addColumnHeader(firstTimeGrain, HEADER_ROW_GROUP1, lastTimeGrain, HEADER_ROW_GROUP1,
                    createTableHeader(new JLabel(day.getLabel())));
//            personsPanel.addColumnHeader(firstTimeGrain, HEADER_ROW_GROUP1, lastTimeGrain, HEADER_ROW_GROUP1,
//                    createTableHeader(new JLabel(day.getLabel())));

        }
    }

    private void fillMeetingAssignmentCells(MeetingSchedule meetingSchedule) {
        TangoColorFactory tangoColorFactory = new TangoColorFactory();
        for (MeetingAssignment meetingAssignment : meetingSchedule.getMeetingAssignmentList()) {
            Color color = tangoColorFactory.pickColor(meetingAssignment.getMeeting());
            TimeGrain startingTimeGrain = meetingAssignment.getStartingTimeGrain();
            TimeGrain lastTimeGrain;
            if (startingTimeGrain == null) {
                lastTimeGrain = null;
            } else {
                int lastTimeGrainIndex = meetingAssignment.getLastTimeGrainIndex();
                List<TimeGrain> timeGrainList = meetingSchedule.getTimeGrainList();
                if (lastTimeGrainIndex < meetingSchedule.getTimeGrainList().size()) {
                    lastTimeGrain = timeGrainList.get(lastTimeGrainIndex);
                } else {
                    lastTimeGrain = OVERTIME_TIME_GRAIN;
                }
            }
            roomsPanel.addCell(startingTimeGrain, meetingAssignment.getRoom(),
                    lastTimeGrain, meetingAssignment.getRoom(),
                    createButton(meetingAssignment, color));
//            for (RequiredAttendance requiredAttendance : meetingAssignment.getMeeting().getRequiredAttendanceList()) {
//                Pair<Person, Boolean> pair = Pair.of(requiredAttendance.getPerson(), Boolean.TRUE);
////                personsPanel.addCell(startingTimeGrain, pair,
////                        lastTimeGrain, pair,
////                        createButton(meetingAssignment, color));
//            }
//            for (PreferredAttendance preferredAttendance : meetingAssignment.getMeeting().getPreferredAttendanceList()) {
//                Pair<Person, Boolean> pair = Pair.of(preferredAttendance.getPerson(), Boolean.FALSE);
////                personsPanel.addCell(startingTimeGrain, pair,
////                        lastTimeGrain, pair,
////                        createButton(meetingAssignment, color));
//            }
        }
    }

    private JPanel createTableHeader(JLabel label) {
        JPanel headerPanel = new JPanel(new BorderLayout());
        headerPanel.add(label, BorderLayout.NORTH);
        headerPanel.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(TangoColorFactory.ALUMINIUM_5),
                BorderFactory.createEmptyBorder(2, 2, 2, 2)));
        return headerPanel;
    }

    private JButton createButton(MeetingAssignment meetingAssignment, Color color) {
        JButton button = SwingUtils.makeSmallButton(new JButton(new MeetingAssignmentAction(meetingAssignment)));
        button.setBackground(color);
        return button;
    }

    private class MeetingAssignmentAction extends AbstractAction {

        private MeetingAssignment meetingAssignment;

        public MeetingAssignmentAction(MeetingAssignment meetingAssignment) {
            super(meetingAssignment.getLabel());
            putValue(SHORT_DESCRIPTION, "<html>Topic: " + meetingAssignment.getMeeting().getTopic() + "<br/>"
//                    + "Date and time: " + defaultIfNull(meetingAssignment.getStartingDateTimeString(), "unassigned") + "<br/>"
//                    + "Duration: " + meetingAssignment.getMeeting().getDurationString() + "<br/>"
//                    + "Room: " + defaultIfNull(meetingAssignment.getRoom(), "unassigned")
                    + "</html>");
            this.meetingAssignment = meetingAssignment;
        }

        @Override
        public void actionPerformed(ActionEvent e) {
        	
        	Desktop desktop = Desktop.isDesktopSupported() ? Desktop.getDesktop() : null;
            if (desktop != null && desktop.isSupported(Desktop.Action.BROWSE)) {
                try {
                	URL url = new URL(this.meetingAssignment.getMeeting().getUrl());
                    desktop.browse(url.toURI());

                } catch (Exception exp) {
                    exp.printStackTrace();
                }
            }
            // TODO Add support for moving meetings like in other examples
//            JOptionPane.showMessageDialog(MeetingSchedulingPanel.this.getTopLevelAncestor(),
//                    "The GUI does not support this action yet.",
//                    "Unsupported in GUI", JOptionPane.ERROR_MESSAGE);
        }

    }

    private static final class OvertimeTimeGrain extends TimeGrain {

        private OvertimeTimeGrain() {
            setGrainIndex(-1);
            setDay(null);
            setStartingMinuteOfDay(-1);
        }

        @Override
        public String getDateTimeString() {
            return "Overtime";
        }

    }

}

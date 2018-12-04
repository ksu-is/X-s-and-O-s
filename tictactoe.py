https://github.com/gabrieledcjr/TicTacToe/blob/master/tictactoeRL.py
https://mrkaluzny.com/tic-tac-toe-javascript-game/

  Link to project: https://codepen.io/TiffanyK/pen/NEVWqq

CSS implemented 
@charset "utf-8";
/* CSS Document */
*{
	margin: 0;
	padding: 0;
}

table{
	border-collapse: collapse;
	border-spacing: 0;
}

#board{
	padding: 0;
	margin: 0 auto;
	margin-top: 25px;
}

#board tr td{
	width: 100px;
	height: 100px;
	border: 1px solid #000000;
	font-family: almendra, "amatic-sc", "annie-use-your-telescope", "architects-daughter";
	font-size: 30px;
	text-align: center;
}

#board tr td:hover{
	background: #000000;
	cursor: pointer;
}

HTML used
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Tic Tac Toe</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js" type="text/javascript" charset="utf-8"></script>
<link type="text/css" rel="stylesheet" href="tictactoe.css" />
</head>
<body>
<table id="board">
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
    </tr>
</table>
	
	
</body>
</html>

Python & JavaScript
$(document).ready(function(){
	var move = 1;
	var play = true;
	
	$("#board tr td").click(function() {
		if ($(this).text()=="" && play){
			if (move % 2==1) {
				$(this).append("X");
			} else {
				$(this).append("O");
			}
			move++;
			if (checkFortheWinner()!=-1 && checkFortheWinner()!="") {
				if(checkFortheWinner() == "X") {
					alert("Victory for Player 1!");
				} else {
					alert("Victory for Player 2!");
				}
				play = false;
			}
		}
	});
	function checkFortheWinner() {
		var space1 = $("#board tr:nth-child(1) td:nth-child(1)").text();
		var space2 = $("#board tr:nth-child(2) td:nth-child(1)").text();
		var space3 = $("#board tr:nth-child(3) td:nth-child(1)").text();
		var space4 = $("#board tr:nth-child(1) td:nth-child(1)").text();
		var space5 = $("#board tr:nth-child(2) td:nth-child(1)").text();
		var space6 = $("#board tr:nth-child(3) td:nth-child(1)").text();
		var space7 = $("#board tr:nth-child(1) td:nth-child(1)").text();
		var space8 = $("#board tr:nth-child(2) td:nth-child(1)").text();
		var space9 = $("#board tr:nth-child(3) td:nth-child(1)").text();
		
		if      ((space1==space2) && (space2==space3)) {return space3; }
		else if ((space4==space5) && (space5==space6)) { return space6; }
		else if ((space7==space8) && (space8==space9)) { return space9; }
		else if ((space1==space4) && (space4==space7)) { return space7; }
		else if ((space2==space5) && (space5==space8)) { return space8; }
		else if ((space3==space6) && (space6==space9)) { return space9; }
		else if ((space1==space5) && (space5==space9)) { return space9; }
		else if ((space3==space5) && (space5==space7)) { return space7; }
		return -1;
	}
});

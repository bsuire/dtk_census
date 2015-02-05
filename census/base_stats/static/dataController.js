
var downloaded = {}            

function dataController($scope,$http) {

    $scope.click = function() {
    
        // on click, get selected variable from select/dropdown menu 
        var select = document.getElementById("select_var");   
        var variable = select.options[select.selectedIndex].value;
        
        // look for variable in "cache"
        if (variable in downloaded){
            
            $scope.census = downloaded[variable];
            return
        }

        // request variable data from server
        var response = $http.get("http://127.0.0.1:8000/data/"+ variable)

        response.success(function(response) {
            
            // update controller data if response if successful    
            $scope.census = response;
            downloaded[variable] = response
        });
    };
}

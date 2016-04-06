/**
 * Created by vitold on 19.03.16.
 */
module.exports = function(grunt) {

    // 1. Вся настройка находится здесь
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        concat: {
            main: {
                src: [
                        'bower_components/jquery/dist/jquery.min.js',
                        'bower_components/bootstrap/dist/js/bootstrap.min.js',
                        'bower_components/bootstrap/js/tooltip.js',
                        'bower_components/bootstrap/js/confirmation.js',
                        'assets/js/load_posts.js'
                    ],
                dest: 'assets/app.js'
                },
            css:{
                src: [
                    'bower_components/bootstrap/dist/css/bootstrap.min.css',
                    'assets/css/style.css',
                ],
                dest: 'assets/app.css'
            }
        },
        uglify: {
            main: {
                files: {
                     //Результат задачи concat
                    'assets/app.min.js': '<%= concat.main.dest %>',

                }
            }
        }
    });

    // 3. Тут мы указываем Grunt, что хотим использовать этот плагин
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');

    // 4. Указываем, какие задачи выполняются, когда мы вводим «grunt» в терминале
    grunt.registerTask('default', ['concat', 'uglify']);

};
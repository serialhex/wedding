#!/usr/bin/env ruby
require "cgi"
require "yaml"

# http://www.ruby-doc.org/stdlib-1.9.3/libdoc/cgi/rdoc/CGI.html
# http://www.ruby-doc.org/stdlib-1.8.7/libdoc/yaml/rdoc/YAML.html

class Rsvp
  def initialize
    @cgi = CGI.new("html4")
  end
  attr_reader :cgi

  def save_data
    params = @cgi.params
    str = params['last-name'].to_s.downcase + "-"
    str += params['first-name'].to_s.downcase
    File.open("rsvp/#{str}.yaml", "w") { |f|
      f << params.to_yaml
    }
    "data saved:<br>\n" + str
  end

  def out_html
    yay_nay=false
    @cgi.out() do
      @cgi.html() do
        @cgi.head() do
          head_str = "<meta http-equiv=\"refresh\" content=\"1; url=http://www.blue-ninja.com/wedding/"
          if @cgi["rsvp-code"].downcase.strip == "mushroom"
            head_str += "good-code.html\">"
            save_data
            yay_nay=true
          else
            head_str += "bad-code.html\">"
          end
          head_str
        end +
        @cgi.body() do
          res="stuff here<br>\n"
          res+=yay_nay.to_s
          res
        end
      end
    end
  end

end

# first-name=moo
# last-name=poop
# rsvp-code=mushroom

rsvp = Rsvp.new
rsvp.out_html
